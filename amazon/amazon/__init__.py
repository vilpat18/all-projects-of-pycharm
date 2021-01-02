from flask import Flask , g
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import app_config
from flask_httpauth import HTTPTokenAuth

# db variable intialisation
db = SQLAlchemy()

# token base authantication
auth = HTTPTokenAuth('Bearer')

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    db.init_app(app)
    migrate = Migrate(app,db)


