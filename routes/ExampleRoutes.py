import json
import os
from flask import Blueprint, request, Response,flash, jsonify,redirect, render_template, url_for,send_from_directory
from controllers import ExampleController
from werkzeug.utils import secure_filename
from helpers import detect
from datetime import date


bp = Blueprint('ExampleRoutes', __name__)

exampleController = ExampleController()

@bp.route('/', methods=['GET'])
def show_penjelasan():
        
        return render_template('beranda.html')


@bp.route('/static/<filename>')
def get_file(filename):
        return send_from_directory('../static', filename)

# fungsi untuk memfilter extensi yang boleh di input user
def allowed_file(filename):
        ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
        return '.' in filename and \
                filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@bp.route('/model', methods=['GET', 'POST'])
def show_model():
        # menangani method GET
        
        if request.method == 'GET':
                return render_template('model.html')
        # menangani method POST
        elif request.method == 'POST':
                # jika tidak ada file yang dikirimkan
                # print(file)
                if 'file' not in request.files:
                        # return request.url
                        flash('Tidak ada file yang dikirim')
                        return render_template('model.html')
                
                file = request.files['file']
                # jika user tidak memilih file dan browser mengirim file tanpa nama file
                if file.filename == '':
                        flash('Tidak ada foto yang dipilih')
                        return redirect(request.url)
                if file and allowed_file(file.filename):
                        filename = secure_filename(file.filename)
                        data_path = os.path.join('static', filename)
                        # menyimpan data gambar
                        file.save(data_path)

                        # melakukan deteksi dengan fungsi detect dalam folder helpers
                        class_name, score= detect.detect(filename)
                        # return class_name
                        # menghapus data gambar yang telah di deteksi
                        # os.remove(data_path)

                        # mendapatkan url gambar
                        file_url = url_for('ExampleRoutes.get_file', filename=filename)
                      
                        # mengembalikan laman model.html dengan nama kelas hasil deteksi
                        return render_template('model.html', class_name=class_name, file_url=file_url, score=round(score,2))
                
                flash('File yang dimasukkan salah')
                return redirect(request.url)
                

@bp.route('/data', methods=['GET'])
def show_data():
        return render_template('data.html')

@bp.route('/kepadatan', methods=['GET', 'POST'])
def show_kepadatan():
        data_kepadatan = exampleController.get_data()
        banyak_data = len(data_kepadatan)
        # return data
        # if request.method == 'GET':
        return render_template('kepadatan.html', data=data_kepadatan, banyak_data=banyak_data)
        # elif request.method == 'POST':
        #         data = request.form
        #         # return data['jml_seluruh_keong']
        #         if len(data['jml_seluruh_keong']) == 0 and len(data['jml_orang']) == 0 and len(data['jml_titik']) == 0 :
        #                 flash('Data yang dimasukkan kurang')
        #                 return render_template('kepadatan.html')
                
        #         # menyimpan data di database
        #         # hasil = exampleController.tes()
        #         # hasil = int(data['jml_seluruh_keong']) / (int(data['jml_orang']) * int(data['jml_titik']))
                
        #         return render_template('kepadatan.html', data=data_kepadatan,banyak_data=banyak_data)

@bp.route('/save-desa', methods=['POST'])
def save_desa():
        data = request.form
        # return data
        create_data_desa = exampleController.create_data_desa(data['nama_desa'], data['jml_orang'])
        # return create_data_desa
        return show_kepadatan()

@bp.route('/kepadatan/<int:id>', methods=['GET'])
def show_kepadatan_by_id(id):

        # mengambil data kepadatan berdasarkan id
        data_id = exampleController.get_data_id(id)
        # return str(data_id)
        return render_template('kepadatan_id.html', data_id = data_id)
        # return str(id);

@bp.route('/save-kepadatan/<int:id>', methods=['POST'])
def save_kepadatan(id):
        data = request.form
        # kepadatan = float(data['jml_keong']) / (float(data ['jml_orang']) * float(data['jml_titik']))

        # return(str(kepadatan))
        # mengambil data kepadatan berdasarkan id
        response = exampleController.save_kepadatan(id,data=data)
        # return(str(id))
        data_id = show_kepadatan_by_id(id)
        return data_id
        # return (data_id)
        # return render_template('kepadatan_id.html', data_id = data_id)
        # return str(id);