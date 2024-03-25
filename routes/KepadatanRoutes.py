from helpers import authRequired
from controllers import KepadatanController
from flask import Blueprint, render_template, request, redirect, url_for, flash

bp = Blueprint('KepadatanRoutes', __name__, static_folder='../', template_folder='../templates/menu')

controller = KepadatanController()

@bp.route('/kepadatan', methods=['GET', 'POST'])
@authRequired.admin_required
def show_kepadatan():
        # GET DATA FROM CONTROLER
        data_kepadatan = controller.get_data()

        # CHECK IF DATA RECEIVED
        if data_kepadatan['message'] == 'success':
                banyak_data = len(data_kepadatan['data'])
                return render_template('kepadatan.html', data=data_kepadatan['data'], banyak_data=banyak_data)
        
        # SOMETHING WRONG HAPPEN
        flash("Terjadi kesahalan di server")
        return redirect(url_for('BerandaRoutes.show_penjelasan'))

@bp.route('/save-desa', methods=['POST'])
@authRequired.admin_required
def save_desa():
        # GET DATA FROM REQUESTS
        data = request.form

        # CREATE DATA IN CONTROLLER
        create_data_desa = controller.create_data_desa(data['nama_desa'], data['jml_orang'])
        
        # IF DATA SAVED
        if create_data_desa['message'] == 'success':
                flash("Data Berhasil di simpan")
                return redirect(url_for('KepadatanRoutes.show_kepadatan'))
        
        # SOMETHING WRONG HAPPEN
        flash("Terjadi kesahalan di server")
        return redirect(url_for('KepadatanRoutes.show_kepadatan'))

@bp.route('/kepadatan/<int:id>', methods=['GET'])
@authRequired.admin_required
def show_kepadatan_by_id(id):
        # GET DATA BASED ON ID
        get_data = controller.get_data_id(id)

        if get_data['message'] == 'success':
                return render_template('kepadatan_id.html', data_id = get_data['data'])
        
        # SOMETHING WRONG HAPPEN
        flash("Terjadi kesahalan di server")
        return redirect(url_for('KepadatanRoutes.show_kepadatan')) 

@bp.route('/save-kepadatan/<int:id>', methods=['POST'])
@authRequired.admin_required
def save_kepadatan(id):
        # GET DATA FROM REQUESTS
        data = request.form

        # FORMULA KEPADATAN --> JUMLAH_KEONG / (JUMLAH_ORANG * JUMLAH_TITIK)
        kepadatan = 0
        if(int(data['jml_orang']) != 0 or int(data['jml_titik']) != 0): # IF DIVIDER != 0
                kepadatan = float(data['jml_keong']) / (float(data['jml_orang']) * float(data['jml_titik']))
                kepadatan = float("{:.2f}".format(kepadatan))


        # SAVE DATA BASED ON ID
        save_data = controller.save_kepadatan(id,data, kepadatan)

        if save_data['message'] == 'success':
                data_id = show_kepadatan_by_id(id)
                return data_id
        
        # SOMETHING WRONG HAPPEN
        flash("Terjadi kesahalan di server")
        return redirect(url_for('KepadatanRoutes.show_kepadatan'))
