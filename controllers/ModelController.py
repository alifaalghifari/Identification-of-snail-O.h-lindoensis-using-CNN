from datetime import datetime
from helpers.connecttion import db

class ModelController(object):
        def __init__(self):
            pass
        def save_file(self, user, nama_gambar, nama_kelas, skor_akurasi):
            try:
                cursor = db.connection.cursor()
                cursor.execute("""INSERT INTO tbl_gambar VALUES(DEFAULT, %s, %s, %s, %s)""", (user, nama_gambar, nama_kelas, skor_akurasi))
                db.connection.commit()
                cursor.close()
                
                return ({'message': 'success'})
            
            except Exception as e:
                return [{"message":"error ", 'data' : e}]