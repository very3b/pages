from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager
import os, sys
from app.config import Config

app=Flask(__name__)

from app import routes



WIN=sys.platform.startswith('win')
if WIN: 
    prefix='sqlite:///'
else:
    prefix='sqlite:////'
    
# DATABASE CONFIG
app.config['SQLALCHEMY_DATABASE_URI']=prefix+os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY']='dev'

app.config.from_object(Config)

#
db=SQLAlchemy(app)
#Login control
login_manager=LoginManager(app)
