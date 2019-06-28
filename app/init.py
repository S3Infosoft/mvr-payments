from flask import Flask
import os

import config

app = Flask(__name__, 
            template_folder = config.TEMPLATES,
            static_folder   = config.STATIC)
    
app.secret_key = config.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s' % config.DATATBASE
