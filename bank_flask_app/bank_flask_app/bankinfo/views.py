from flask import jsonify,request,Blueprint
from bank_flask_app import db
from bank_flask_app.bankinfo.models import Bankinfo

mod = Blueprint('/bankinfo',__name__,url_prefix='/bankinfo')

@mod.route('/insert_info', methods=['POST'])
def insert_info():
    request_data = request.get_json()
    b_names = Bankinfo(
            bank_name = request_data['bank_name'],
            bank_state = request_data['bank_state'],
            ifsc_code=request_data['ifsc_code']
                )
    db.session.add(b_names)
    db.session.commit()
    return 'successfully added the bank details'

