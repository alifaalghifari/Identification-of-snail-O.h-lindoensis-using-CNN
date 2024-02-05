import json
import os
from flask import Blueprint, request, Response,flash, jsonify,redirect, render_template, url_for,send_from_directory
from controllers import AuthController
from werkzeug.utils import secure_filename
from helpers import detect
from datetime import date

auth = Blueprint('AuthRoutes', __name__)

authController = AuthController()

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('Auth/register.html')
    else:
        # return request.form['nama']
        nama = request.form['nama']
        password = request.form['password']

        register_user = authController.register(nama, password)

        return render_template("Auth/register.html")
