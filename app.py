from flask import Flask
from handlers.routes import configure_routes
import MySQLdb
from flask_cors import CORS
from dotenv import load_dotenv
from flask_session import Session
import os

load_dotenv()

app = Flask(__name__)

configure_routes(app)

CORS(app)

app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_USE_SIGNER'] = True
app.config['SECRET_KEY'] = 'ananasma'
Session(app)

app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')

mysql = MySQLdb.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    db=app.config['MYSQL_DB']
)

if __name__ == '__main__':
    app.run(debug=True)
