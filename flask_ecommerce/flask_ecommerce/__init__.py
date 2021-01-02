from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import app_config


db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    db.init_app(app)

    from flask_ecommerce.users.views import mod as user_module

    app.register_blueprint(user_module)
    return app

 