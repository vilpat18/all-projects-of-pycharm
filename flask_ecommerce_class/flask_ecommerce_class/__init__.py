from flask import Flask, g
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPTokenAuth
from config import app_config

db = SQLAlchemy()
# database initialization

auth = HTTPTokenAuth('Bearer')
# Token based auth

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    db.init_app(app)
    migrate = Migrate(app,db)

    from flask_ecommerce_class.users.views import mod as user_module

    app.register_blueprint(user_module)
    return app
