from flask import jsonify,Blueprint,request
from bank_flask_app import db
from bank_flask_app.customers.models import Customers

mod = Blueprint('/customers',__name__,url_prefix='/customers')

@mod.route('customer_info',methods=['POST'])
def customer_info():
    request_data= request.get_json()
    cust_info = Customers(
        bank_id=request_data['bank_id'],
        cust_name=request_data['cust_name'],
        city = request_data['city'],
        acc_id = request_data['acc_id'])
    db.session.add(cust_info)
    db.session.commit()
    return "customers info added successfully"