from flask import Blueprint,jsonify,request
from bank_flask_app.account.models import Account
from bank_flask_app import db

mod = Blueprint('/account',__name__,url_prefix='/account')

@mod.route('/add_account_details',methods=['POST'])
def add_account_details():
    request_data = request.get_json()
    account_d = Account(
        acc_number = request_data['acc_number'],
        acc_balance = request_data['acc_balance']
                  )
    db.session.add(account_d)
    db.session.commit()
    return "account detalis uploaded successfully"
