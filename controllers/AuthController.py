from flask import jsonify
from helpers.connecttion import db
from werkzeug.security import generate_password_hash, check_password_hash

class AuthController(object):
    def __init__(self):
        pass
    def register(self,username,password,email):
        password = generate_password_hash(password, method='sha256')
        try:
            cursor = db.connection.cursor()

            cursor.execute("""INSERT INTO tbl_user VALUES(DEFAULT, %s, %s, %s, DEFAULT)""", (username, password, email))

            db.connection.commit()
            cursor.close()

            return {'message': 'success'}
        except Exception as e:
            return {'message' : 'Username atau Email sudah terpakai'}
    
    def login(self, username, password):
        cursor = db.connection.cursor()

        cursor.execute("""SELECT * FROM tbl_user WHERE nama=(%s)""", (username,))

        get_user = cursor.fetchall()

        # CHECK IF USER EXIST
        if len(get_user) == 0:
            return {'message' : 'Akun tidak ditemukan'}
        
        # CHECK IF PASSWORD IS SAME
        if check_password_hash(get_user[0][2],password):
            return {'message': 'success', 'data' : get_user}
        else:
            return {'message' : 'Password salah'}
