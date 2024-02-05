from config import configuration, http

# import MySQLdb
from datetime import date


app = http.create_app(configuration.Configuration)

port = int(configuration.Configuration.PORT)
# mysql = MySQL(app)

# app = Flask(__name__, template_folder='../templates', static_folder='upload')
#     # print(configuration)
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'tugas_akhir'



if __name__ == "__main__":

     app.run(host="0.0.0.0", port=port, debug=True)
set