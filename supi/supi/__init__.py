from flask import Flask


def create_app():
    app = Flask(__name__)

    from supi.billing.views import mod as biiling_module

    app.register_blueprint(biiling_module)
    return app