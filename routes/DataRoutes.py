from flask import Blueprint, render_template

from helpers import authRequired

bp = Blueprint('DataRoutes', __name__)

@bp.route('/data', methods=['GET'])
@authRequired.login_required
def show_data():
        return render_template('menu/data.html')