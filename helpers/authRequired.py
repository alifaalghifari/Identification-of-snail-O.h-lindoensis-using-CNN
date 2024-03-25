from functools import wraps
from flask import session, redirect, url_for

def login_required(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
                if 'username' not in session:
                # Redirect to login page if user is not logged in
                        return redirect(url_for('AuthRoutes.login'))
                return f(*args, **kwargs)
        return decorated_function

def admin_required(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
                if 'is_admin' not in session:
                # Redirect to login page if user is not logged in
                        return redirect(url_for('ExampleRoutes.show_penjelasan'))
                return f(*args, **kwargs)
        return decorated_function