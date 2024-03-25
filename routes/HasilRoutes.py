import os
from helpers import authRequired
from controllers import HasilController
from flask import Blueprint, render_template, session, redirect, url_for, flash

bp = Blueprint('HasilRoutes', __name__)

controller = HasilController()

@bp.route('/hasil', methods=['GET'])
@authRequired.login_required
def show_data():
        user = session.get('username')

        get_data = controller.get_file_user(user)

        if get_data['message'] == 'success':
                return render_template('menu/hasil.html', data = get_data['data'], folder=user)
        flash('Terjadi kesalahan di server')
        return redirect(url_for('BerandaRoutes.show_penjelasan'))
@bp.route('/hapus/<path:filename>', methods=['POST'])
@authRequired.login_required
def delete_file(filename):
        user = session.get('username')
        path_file = os.path.join('uploads', user, filename)
        if os.path.exists(path_file):
                delete_data = controller.delete_file_user(user, filename)
                if(delete_data['message'] == 'success'):
                        # DELETE DATA IN FOLDER USER
                        os.remove(path_file)
                        flash('Data berhasil di hapus')
                else:
                        flash('Terjadi kesalahan di server')
        else:
                flash('Data tidak ditemukan')
        return redirect(url_for('HasilRoutes.show_data'))