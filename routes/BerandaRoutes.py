from flask import Blueprint, render_template

from helpers import authRequired


bp = Blueprint('BerandaRoutes', __name__)


@bp.route('/', methods=['GET'])
@authRequired.login_required
def show_penjelasan():
        return render_template('menu/beranda.html')

