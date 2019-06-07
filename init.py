from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

secret_key = os.urandom(12).hex()

app = Flask(__name__)
app.secret_key = secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/database.db'

db = SQLAlchemy(app)