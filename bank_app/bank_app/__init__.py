from flask import Flask

def create_app():
    app = Flask(__name__)

    from bank_app.bank.view import mod as bank_module
    from bank_app.customer.view import mod as customer_module
    from bank_app.account.view import mod as account_module
    from bank_app.transaction.view import mod as transaction_module

    app.register_blueprint(bank_module)
    app.register_blueprint(customer_module)
    app.register_blueprint(account_module)
    app.register_blueprint(transaction_module)
    return app




