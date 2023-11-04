from flask import Flask
from handlers.routes import configure_routes
from flask_cors import CORS
import pymysql  # Import PyMySQL
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

# Configure your MySQL connection using PyMySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = os.getenv('mp_db')

# Create a PyMySQL connection
mysql = pymysql.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    db=app.config['MYSQL_DB']
)

if __name__ == '__main__':
    app.run(debug=True)