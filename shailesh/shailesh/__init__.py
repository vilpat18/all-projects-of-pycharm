from flask import Flask


def create_app():

    app = Flask(__name__)

    from shailesh.appointment.view import mod as appointment_module
    from shailesh.customer.view import mod as customer_module
    from shailesh.employee.view import mod as employee_module
    from shailesh.payment.view import mod as payment_module
    from shailesh.services.view import mod as services_module

    app.register_blueprint(appointment_module)
    app.register_blueprint(customer_module)
    app.register_blueprint(employee_module)
    app.register_blueprint(payment_module)
    app.register_blueprint(services_module)
    return app