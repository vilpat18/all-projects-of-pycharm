from flask import Flask, g
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import app_config
from flask_httpauth import HTTPTokenAuth

# db variable initialization
db = SQLAlchemy()
# Token based auth
auth = HTTPTokenAuth('Bearer')

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    db.init_app(app)
    migrate = Migrate(app, db)

    # Import a module / component using its blueprint handler variable
    # from flask_ecommerce.users.views_json import mod as json_users_module
    from ecommerce.product.views import mod as users_module
    from ecommerce.role.views import mod as role_module
    from ecommerce.admin.views import mod as admin_module
    from ecommerce.customer.views import mod as customer_module
    from ecommerce.vendor.views import mod as vendors_module
    from ecommerce.order.views import mod as order_module
    # Register blueprint(s)
    # app.register_blueprint(json_users_module)
    app.register_blueprint(users_module)
    app.register_blueprint(role_module)
    app.register_blueprint(admin_module)
    app.register_blueprint(customer_module)
    app.register_blueprint(vendors_module)
    app.register_blueprint(order_module)
    return app