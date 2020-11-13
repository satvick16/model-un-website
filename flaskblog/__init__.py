from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba248'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://jighdpllfrixlw:adf9336c5c2395a561c0b403cf4d7fd95ea8579539c6737f071463e956355c23@ec2-3-218-75-21.compute-1.amazonaws.com:5432/d733jsgo4ibd7u"
SQLALCHEMY_TRACK_MODIFICATIONS = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskblog import routes
