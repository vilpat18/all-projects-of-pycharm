from config import app_config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    db.init_app(app)

    from bank_flask_app.bankinfo.views import mod as bankinfo_module
    from bank_flask_app.customers.views import mod as customer_module
    from bank_flask_app.account.views import mod as account_module
    from bank_flask_app.transaction.views import mod as transaction_module


    app.register_blueprint(bankinfo_module)
    app.register_blueprint(customer_module)
    app.register_blueprint(account_module)
    app.register_blueprint(transaction_module)
    return app



