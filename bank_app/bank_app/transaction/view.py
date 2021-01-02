from flask import jsonify,Blueprint,request
import json
from datetime import datetime

mod = Blueprint('transaction',__name__,url_prefix='/transaction')

transaction_data = json.load(open("transaction.json",'r'))
customer_data = json.load(open("customer.json",'r'))
account_data = json.load(open("acount.json",'r'))

@mod.route('/transfer',methods=['POST'])
def transaction_info():
    account_id_from = int(request.form.get('account_balance_from'))
    account_id_to = int(request.form.get('account_balance_to'))
    amount_transfer = int(request.form.get('transfer_amt'))
    now =datetime.now()
    date_time = now.strftime("%d/%m/%Y %H:%M:%S")
    #transaction_id=int(request.form.get('transaction_id'))
    print(account_id_from,account_id_to,amount_transfer)
    if transaction_data==[]:
        transaction_id=1
    else:
        transaction_id=transaction_data[-1]["transaction_id"]+1

    for i in account_data:
          for j in account_data:
                 if i['account_id'] == account_id_from and j['account_id'] == account_id_to:
                      if i['account_balance'] >= amount_transfer:
                           i['account_balance'] = i['account_balance'] - amount_transfer
                           j['account_balance'] = j['account_balance'] + amount_transfer



          response={'transaction_id':int(transaction_id),
                  "account_from": i["account_id"],
                  "account_to": j['account_id'],
                  "account_balance_from":i['account_balance'],
                  "account_balance_to": j["account_balance"],
                  'transfer_amt':int(amount_transfer),
                  'date_time':date_time}

          transaction_data.append(response)
          json.dump(account_data,open('acount.json','w'))
          json.dump(transaction_data, open('transaction.json', 'w'))
          return "hiiiii"

@mod.route('/deposite',methods=['PUT'])
def deposite():
    act_to_deposite=int(request.form.get("id"))
    amount_to_deposite=int(request.form.get("amt"))
    print(act_to_deposite,amount_to_deposite)

    for i in account_data:
        if i['account_id'] == act_to_deposite:
            i['account_balance'] += amount_to_deposite
            response={'id':act_to_deposite,
                      'amt':amount_to_deposite}
            account_data.append(response)
            json.dump(account_data, open('acount.json', 'w'))

        elif i['account_id']!= act_to_deposite:
              print("pls enter valid id")
    return "money deposited successfully"



@mod.route('/withdraw',methods=['POST'])
def withdraw():
    act_to_withdraw = int(request.form.get('account_id'))
    amount_to_withdraw =request.form.get('account_balance')
    print(act_to_withdraw,amount_to_withdraw)
    for j in account_data:
        if int(amount_to_withdraw) < j['account_balance']:
            print("insufficient balance")
        else:
            if j["account_id"] == act_to_withdraw:
                j['account_balance'] = j['account_balance'] - int(amount_to_withdraw)
            response={'account_id':act_to_withdraw,
                     'account_balance':amount_to_withdraw }
            transaction_data.append(response)
            json.dump(account_data, open('acount.json', 'w'))
            return jsonify(account_data)










