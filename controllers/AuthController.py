from config.configuration import Configuration
# from config import configuration, http
# from flask import Flask
# from flask_mysqldb import MySQL
from helpers.connecttion import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class AuthController(object):
    def __init__(self):
        pass
    def register(self,nama,password):
        cursor = db.connection.cursor()

        now = datetime.now()
        id_gambar = nama + "_"  + str(now)
        print(id_gambar)
        password = generate_password_hash(password, method='sha256')
        
        regis = cursor.execute("""INSERT INTO tbl_user VALUES(DEFAULT, %s, %s, %s)""", (nama, password,id_gambar))

        db.connection.commit()
        cursor.close()
        return regis
    
    