from flask import json,jsonify,Blueprint,request

mod = Blueprint('billing',__name__,url_prefix='/billing')

billing_data =json.load(open('billing.json','r'))

@mod.route('/billing_info',methods=['POST'])
def biiling():
    reciept_no = request.form.get('reciept_no')
    customer_id = request.form.get('customer_id')
    customer_name = request.form.get('customer_name')
    vehicle_tyep_model = request.form.get('vehicle_tyep_model')

    response = { 'reciept_number': (reciept_no),
                 'customer_id': (customer_id),
                 'customer_name':(customer_name),
                 'vehicle_type': (vehicle_tyep_model)  }

    billing_data.append(response)
    json.dump(billing_data,open('billing.json','w'))
    return jsonify(response)



