from flask import Flask
import os

from config import __secret_key__ 

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.secret_key = __secret_key__
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
