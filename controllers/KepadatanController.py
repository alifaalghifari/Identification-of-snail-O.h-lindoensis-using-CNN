from datetime import datetime
from helpers.connecttion import db

class KepadatanController(object):
        def __init__(self):
            pass

        def create_data_desa(self,nama_desa, jml_orang):
            try:
                now = datetime.now()    
                cursor = db.connection.cursor()
                cursor.execute("""INSERT INTO tbl_kepadatan_keong VALUES(DEFAULT, %s, DEFAULT, %s, DEFAULT, DEFAULT, %s)""", (nama_desa, jml_orang, now.date()))
                db.connection.commit()
                cursor.close()

                return ({'message' : 'success'})
            
            except Exception as e:
                return [{"message":"error ", 'data' : e}]
            
        
        def get_data(self):
            try:
                cursor = db.connection.cursor()
                cursor.execute("""SELECT * FROM tbl_kepadatan_keong""")
                data = cursor.fetchall()
                cursor.close()

                return ({'message' : 'success',  'data' : data})
            
            except Exception as e:
                return ({'message' : 'error', 'data': e})

        def get_data_id(self, id):
            try:
                cursor = db.connection.cursor()
                cursor.execute("""SELECT * FROM tbl_kepadatan_keong WHERE id=%s""", (id,))
                data_id = cursor.fetchall()
                cursor.close()

                return ({'message' : 'success',  'data' : data_id})

            except Exception as e:
                return ({'message' : 'error', 'data': e})
                
        
        def save_kepadatan(self,id,data,kepadatan):
            try:
                cursor = db.connection.cursor()
                update = cursor.execute("""UPDATE tbl_kepadatan_keong SET jml_keong=%s, jml_orang=%s, jml_titik=%s, hasil=%s  WHERE id=%s""", (data['jml_keong'], data['jml_orang'], data['jml_titik'], kepadatan, id))
                db.connection.commit()
                cursor.close()
                
                return ({'message' : 'success', 'data' : update})
            
            except Exception as e:
                return ({'message' : 'error', 'data': e})