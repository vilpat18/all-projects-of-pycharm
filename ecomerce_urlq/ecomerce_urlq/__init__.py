from flask import Flask

def create_app():
    app = Flask(__name__)


    from ecomerce_urlq.users.view import mod as user

    app.register_blueprint(user)
    return app




