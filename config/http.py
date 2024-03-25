import routes
from flask import Flask
from flask_cors import CORS
from flask_mysqldb import MySQL
from helpers.connecttion import db
from flask_compress import Compress

cors = CORS()
compress = Compress()

def create_app(configuration):
    app = Flask(__name__.split(',')[0], template_folder='../templates', static_folder='../static')

    # REGISTER ROUTE BLUEPRINT MENU
    app.register_blueprint(routes.DataRoutes.bp)
    app.register_blueprint(routes.ModelRoutes.bp)
    app.register_blueprint(routes.BerandaRoutes.bp)
    app.register_blueprint(routes.HasilRoutes.bp)
    app.register_blueprint(routes.KepadatanRoutes.bp)

    # REGISTER ROUTE BLUEPRINT AUTH
    app.register_blueprint(routes.AuthRoutes.auth)

    app.config.from_object(configuration)
    db.init_app(app)

    cors.init_app(app, resources={r"/*": {"origins": "*"}})
    compress.init_app(app)

    return app

def create_mysql():
    app = create_app()
    mysql = MySQL(app)
    return mysql