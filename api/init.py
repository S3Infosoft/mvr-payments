from flask import Flask
secret_key = 'b56bcfe6e990f28915f5a7c3'

app = Flask(__name__)
app.secret_key = secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database/database.db'
app.config['TESTING'] = False