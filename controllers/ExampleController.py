from config.configuration import Configuration
# from config import configuration, http
# from flask import Flask
# from flask_mysqldb import MySQL
from helpers.connecttion import db

from datetime import datetime


# mysql = MySQL(app())

class ExampleController(object):
        def __init__(self):
            pass
        def hello(self):
            try:
                return [{"msg":"hello"}]
            except Exception as e:
                # fail response
                return [{"msg":"error "+e}]
        def create_data_desa(self,nama_desa, jml_orang):
            cursor = db.connection.cursor()
            # hari_ini = date.today()
            now = datetime.now()    
            # return now
            tes = cursor.execute("""INSERT INTO tbl_kepadatan_keong VALUES(DEFAULT, %s, DEFAULT, %s, DEFAULT, DEFAULT, %s)""", (nama_desa, jml_orang, now.date()))
            db.connection.commit()
            cursor.close()
            return tes
        
        def get_data(self):
            cursor = db.connection.cursor()
            # hari_ini = date.today()
            cursor.execute("""SELECT * FROM tbl_kepadatan_keong""")
            data = cursor.fetchall()
            cursor.close()
            return data

        def get_data_id(self, id):
            #  return id
            cursor = db.connection.cursor()
            cursor.execute("""SELECT * FROM tbl_kepadatan_keong WHERE id=%s""", (id,))
            data_id = cursor.fetchall()
            
            cursor.close()
            return data_id
        
        def save_kepadatan(self,id,data):
            cursor = db.connection.cursor()
            if(int(data['jml_orang']) == 0 or int(data['jml_titik']) == 0):
                kepadatan = 0
            else:
                kepadatan = float(data['jml_keong']) / (float(data['jml_orang']) * float(data['jml_titik']))
                kepadatan = float("{:.2f}".format(kepadatan))

            saving = cursor.execute("""UPDATE tbl_kepadatan_keong SET jml_keong=%s, jml_orang=%s, jml_titik=%s, hasil=%s  WHERE id=%s""", (data['jml_keong'], data['jml_orang'], data['jml_titik'], kepadatan, id))

            db.connection.commit()
            cursor.close()
            return saving