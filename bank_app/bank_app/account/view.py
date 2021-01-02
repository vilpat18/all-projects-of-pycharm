from flask import jsonify,Blueprint,request
import json

mod = Blueprint('account',__name__,url_prefix='/account')

account_data = json.load(open('acount.json','r'))

@mod.route('/account_info',methods=['POST'])
def account_info():

    a_no = request.form.get("account_no")
    a_balance = request.form.get("account_balance")
    if account_data==[]:
        a_id=1
    else:
        a_id=account_data[-1]['account_id']+1

    response={"account_id":int(a_id),
              "account_no":int(a_no),
              "account_balance":int(a_balance)}

    account_data.append(response)
    json.dump(account_data,open("acount.json",'w'))
    return jsonify(response)

