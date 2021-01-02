from flask import Flask

def create_app():
    app=Flask(__name__)

    from calculation.calculator.view import mod

    app.register_blueprint(mod)

    return app
