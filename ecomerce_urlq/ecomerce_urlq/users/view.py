from flask import Blueprint,jsonify,request
import json


mod = Blueprint('users',__name__,url_prefix="/users")

data = json.load(open("data.json","r"))


@mod.route('/create_users_json_req',methods=['POST'])
def create_users_json_request():
    #print(jsonify(data))

    request_data = request.get_json()
    reasponse = request_data
    data.append(reasponse)
    json.dump(data,open('data.json','w'))
    return jsonify(reasponse)




    #username=request_data['username']
    #password=request_data['password']
    #new_user_id = data[-1]['id']+1
   #reaponse=request_data
    #reaponse['id']=new_user_id
    #reaponse['username']=username
    #reaponse['password']=password
   # data.append(reaponse)
   # json.dump(data,open('data.json','w'))
   #return jsonify(reaponse)





