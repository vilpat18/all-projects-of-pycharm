from flask import jsonify, Blueprint, request , json


mod = Blueprint('bank',__name__,url_prefix='/bank')

bank_data= json.load(open("bank.json",'r'))

@mod.route('/create_bank',methods=['POST'])
def bank_info():

    #bank_id = request.form.get("bank_id")
    bank_name=request.form.get("bank_name")
    bank_state=request.form.get("bank_state")
    if bank_data==[]:
        new_user_id=1
    else:
        new_user_id = bank_data[-1]['bank_id'] + 1

    response={'bank_id': new_user_id,
              "bank_name":bank_name,
              "bank_state":bank_state}
    bank_data.append(response)
    json.dump(bank_data,open("bank.json",'w'))
    return jsonify(response)
