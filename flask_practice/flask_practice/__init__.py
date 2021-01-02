from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import app_config
from flask_migrate import Migrate
from flask_httpauth  import HTTPTokenAuth

db = SQLAlchemy() #db variable initializaton
auth = HTTPTokenAuth('bearer')


def create_app(config_name):
    app =Flask(__name__)
    app.config.from_object(app_config[config_name])
    db.init_app(app)
    migrate = Migrate(app,db)


    from flask_practice.users.views import mod as users_module

    app.register_blueprint(users_module)
    return app

