from flask import Blueprint,jsonify,request
from bank_flask_app import db
from bank_flask_app.transaction.models import Transaction
from bank_flask_app.customers.models import Customers
from bank_flask_app.account.models import Account

mod = Blueprint('/transaction',__name__,url_prefix='/transaction')

@mod.route('/add_transaction',methods=['post'])
def transaction():
    request_data = request.get_json()
    trans = Transaction(
        cst_id_from = request_data(int('cst_id_from')),
        cst_id_to = request_data(int('cst_id_to')),
        acc_type = request_data('acc_type'))

    db.session.add(trans)
    db.session.commit()
    return 'transaction successfull'
