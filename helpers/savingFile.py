import os
from flask import session

# FILTER EXTENCTION FROM USER
def allowed_file(filename):
        ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
        return '.' in filename and \
                filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_file(file):
        # CHECK IF FOLDER EXIST
        user_folder = session.get('username')
        user_path = 'uploads/'+ user_folder
        if not os.path.exists(user_path):
                os.makedirs(user_path)
        try:
                # ADD FILE NAME A SUFFIX
                filename = file.filename 
                # SAVE FILE 
                file_path = os.path.join(user_path, filename)
                # CHECK IF IMAGE EXIST
                if os.path.exists(file_path):
                        return ({'message' : 'exist'})
                file.save(file_path)

                return ({'message' : 'succes','folder' : user_folder, 'filename' : filename})
        except Exception as e:
                return e