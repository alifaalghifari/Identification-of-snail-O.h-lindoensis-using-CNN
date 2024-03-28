import os
from controllers import ModelController
from helpers import authRequired, detect, savingFile
from werkzeug.utils import secure_filename
from flask import Blueprint, render_template, request, flash, redirect, url_for, send_from_directory, session

bp = Blueprint('ModelRoutes', __name__)

controller = ModelController()

@bp.route('/uploads/<folder>/<path:filename>')
def get_file(folder, filename):
        path_dir = os.path.join('../uploads', folder )

        return send_from_directory(path_dir, filename)

@bp.route('/model', methods=['GET', 'POST'])
@authRequired.login_required
def show_model():
        # menangani method GET
        if request.method == 'GET':
                return render_template('menu/model.html')
        # menangani method POST
        elif request.method == 'POST':
                # NO FILE
                if 'file' not in request.files:
                        flash('Tidak ada file yang dikirim')
                        return render_template('menu/model.html')
                
                file = request.files['file']

                # IF FILE DON'T HAVE NAME
                if file.filename == '':
                        flash('Tidak ada foto yang dipilih')
                        return redirect(request.url)
                
                if file and savingFile.allowed_file(file.filename):
                        # filename = secure_filename(file.filename)

                        # SAVE FILE ON USER FOLDER
                        data_save = savingFile.save_file(file)

                        if(data_save['message'] == 'exist'):
                                flash('Gambar sudah diklasifikasi, cek menu Hasil Klasifikasi')
                                return render_template('menu/model.html')
                        
                        # DETECT IMAGE
                        data_detect= detect.detect_lite(folder=data_save['folder'], filename=data_save['filename'])
                        
                        # return data_detect
                        
                                # return redirect(url_for('BerandaRoutes.show_penjelasan'))
                        # SAVE TO DB
                        user = session.get('username')
                        saving_file = controller.save_file(user, data_save['filename'], data_detect['class name'], data_detect['score'])

                        if(saving_file['message'] == 'success'):
                                flash('File berhasil di klasifikasi !')
                        # mengembalikan laman model.html dengan nama kelas hasil deteksi
                        return render_template('menu/model.html', class_name=data_detect['class name'], folder=data_save['folder'], filename=data_save['filename'], score=round(data_detect['score'],2))
                
                flash('File yang dimasukkan salah')
                return redirect(request.url)