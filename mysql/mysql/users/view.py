from flask import jsonify,Blueprint,request
import json


mod = Blueprint('users',__name__,url_prefix='/users')

#fp = open("data.json",'r')
#data = json.loads(fp)

data = json.load(open("data.json","r"))

@mod.route("/login",methods=['GET'])
def fetch():
    return jsonify(data)

@mod.route('/<user_id>',methods=['GET'])
def show(user_id):
    print('user_id:',user_id)
    reponse={'id':x[id] for x in data if x['id']==int(user_id)}
    return jsonify(reponse)
@mod.route("/login",methods=['POST'])
def homepage():
    return "success"


@mod.route('/create_users_json_req', methods=['POST'])
def create_users_json_request():
    request_data = request.get_json()
    username = request_data['username']
    password = request_data['password']
    new_user_id = data[-1]['id'] + 1
    reaponse = request_data
    reaponse['id'] = new_user_id
    reaponse['username'] = username
    reaponse['password'] = password
    data.append(reaponse)
    json.dump(data, open('data.json', 'w'))
    return jsonify(reaponse)

@mod.route('/create_users_form_req',methods=['POST'])
def create_users_form_request():
    print('request_data:',request.form.to_dict())
    username=request.form.get('username')
    password=request.form.get('password')
    new_user_id = data[-1]['id']+1
    reaponse={'id':new_user_id,
              "username":username,
              "password":password}
    data.append(reaponse)
    json.dump(data,open('data.json','w'))
    return jsonify(reaponse)

@mod.route('/update_user/<user_id>',methods=["PUT"])
def update_user(user_id):

    request_data = request.get_json()
    print("request_data:",request_data)
    for d in data:
        if d['id']==int(user_id):
            if 'username' in request_data:
                d["username"]=request_data["username"]

            if 'password' in request_data:
                d["password"]=request_data['password']

    json.dump(data,open("data.json",'w'))
    return "user details update"



@mod.route('/delete_user/<user_id>',methods=["DELETE"])
def delete_user(user_id):

    for index,d in enumerate(data):
       if d in data:
        if d['id']==int(user_id):
            del data[index]
    json.dump(data,open("data.json",'w'))
    return "user details update"