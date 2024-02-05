import os
from dotenv import load_dotenv, find_dotenv
# Load environment
load_dotenv(find_dotenv())
app_code = os.getenv("APP_CODE")
class Configuration(object):
     # Basic
     DEBUG = os.getenv("DEBUG") == "True"
     PORT = int(os.getenv("PORT", 5000))
     UPLOAD_FOLDER = '../upload'
     SECRET_KEY='my secret'

     MYSQL_HOST = 'localhost'
     MYSQL_USER = 'root'
     MYSQL_PASSWORD = ''
     MYSQL_DB = 'tugas_akhir'