from helpers.connecttion import db

class HasilController(object):
        def __init__(self):
            pass
        def get_file_user(self, user):
            try:
                cursor = db.connection.cursor()
                cursor.execute("""SELECT * FROM tbl_gambar WHERE user=(%s)""", (user,))
                data = cursor.fetchall()
                cursor.close()
                
                return ({'message': 'success', 'data' : data})
            
            except Exception as e:
                return ({'message' : 'error', 'data' : e})
        
        def delete_file_user(self, user, filename):
            try:
                cursor = db.connection.cursor()
                cursor.execute("""DELETE FROM tbl_gambar WHERE user=(%s) AND nama_gambar=(%s)""", (user, filename))
                db.connection.commit()
                cursor.close()

                return ({'message': 'success'})
            
            except Exception as e:
                return ({'message' : 'error', 'data' : e})