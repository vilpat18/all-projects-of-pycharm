from flask import jsonify, Blueprint, request
import json

mod = Blueprint('customer', __name__, url_prefix='/customer')

customer_data = json.load(open("customer.json", 'r'))


@mod.route("/customer_info", methods=['POST'])
def customer_info():


    c_name=request.form.get("customer_name")
    c_state=request.form.get("customer_state")
    c_acc_id=request.form.get("customer_acc_id")
    c_bank_id=request.form.get("customer_bank_id")
    if customer_data==[]:
        c_id=1
    else:
        c_id=customer_data[-1]["customer_id"]+1

    response={"customer_id":c_id,
              "customer_name":c_name,
              "customer_state":c_state,
              "customer_acc_id":c_acc_id,
              "customer_bank_id":c_bank_id}
    customer_data.append(response)
    json.dump(customer_data, open("customer.json", 'w'))
    return jsonify(response)

