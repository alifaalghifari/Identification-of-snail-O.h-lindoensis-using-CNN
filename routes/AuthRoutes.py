from controllers import AuthController
from helpers import validatePassword
from flask import Blueprint, request, redirect, render_template, url_for, session, flash

auth = Blueprint('AuthRoutes', __name__)

authController = AuthController()

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('Auth/register.html')
    else:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        # RETURN IF USERNAME OR PASSWORD NOT PROVIDED
        if not username or not password:
            flash('Username, email dan password diperlukan')
            return render_template("Auth/register.html")
        
        if not validatePassword.validate_password(password):
            flash(validatePassword.PASSWORD_COMPLEXITY_ERROR)
            return render_template("Auth/register.html")
            
        register_user = authController.register(username, password, email)

        if(register_user['message'] == 'success'):
            flash('Akun berhasil dibuat')
            return render_template("Auth/login.html")

        flash(register_user['message'])
        return render_template("Auth/register.html")
    
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('Auth/login.html')
    else:
        username = request.form['username']
        password = request.form['password']

        # RETURN IF USERNAME OR PASSWORD NOT PROVIDED
        if not username or not password:
            flash('Username dan password diperlukan')
            return render_template("Auth/login.html")

        register_user = authController.login(username, password)

        if(register_user['message'] == 'success'):

            # SET SESSION
            session['username'] = username

            # CHECK IS ADMIN
            if register_user['data'][0][4] == 1:
                # SET SESSION ADMIN
                session['is_admin'] = True
            
            return redirect(url_for("BerandaRoutes.show_penjelasan"))
        
        # RETURN IF USERNAME OR PASSWORD IS WRONG
        flash(register_user['message'])
        return render_template("Auth/login.html")

@auth.route('/logout', methods=['POST'])
def logout():
    session.pop('username', None)

    # DELETE SESSION IS_ADMIN IF EXIST
    if 'is_admin' in session:
        session.pop('is_admin', None)

    return redirect(url_for("AuthRoutes.login"))
