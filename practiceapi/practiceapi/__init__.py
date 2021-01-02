from flask import Flask

def create_app():
    app = Flask(__name__)

    #import a module /component using it blueprint
    from practiceapi.users.view import mod as users_module

    #register blueprint
    app.register_blueprint(users_module)
    return app