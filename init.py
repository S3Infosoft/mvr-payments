from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = '123456789'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/database.db'

db = SQLAlchemy(app)