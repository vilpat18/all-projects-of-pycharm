from datetime import datetime
from functools import wraps
import jwt
import uuid
from flask import jsonify, request, Blueprint, app, make_response
from werkzeug.security import generate_password_hash, check_password_hash


from flaskAPI.user.models import Users ,Authors
from flaskAPI import db

mod = Blueprint('users',__name__,url_prefix='/users')


def token_required(f):
    @wraps(f)
    def decoretor(*args, **kwargs):
        token = None

        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']
        if not token :
            return jsonify({'message':'a valid token is missing'})

        try:
            data = jwt.decode(token,app.config[SECRET_KEY])
            current_user = Users.query.filter_by(public_id=data['public_id']).first()
        except:
            return jsonify({'message':'token is invalid'})
        return f(current_user,*args, **kwargs)
    return decoretor()


@mod.route('/register',methods=['GET','POST'])
def sign_up():
    data = request.get_json()
    hash_password = generate_password_hash(data['passsword'],method='shah256')
    new_user = Users(public_id=str(uuid.uuid4()),name=data['name'],password=hash_password,admin=False)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'msg':'registerd successfully'})

@mod.route('/login',methods=['GET','POST'])
def login():
    auth = request.authorization
    if not auth or not auth.username or auth.password:
        return make_response('could not verify',401,{'WWW.Authentication': 'Basic realm: "login required"'})

    user = Users.query.filter_by(name=auth.username).first()
    if check_password_hash(user.password,auth.password):
        token = jwt.decode({'public_id':user.public_id,'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=30)},
                           app.config ['SECRET_KEY'])
        return jsonify({'token': token.decode('UTF-8')})

    return make_response('could not verify', 401, {'WWW.Authentication': 'Basic realm: "login required"'})



@mod.route('/users', methods=['GET'])
def get_all_users():

   users = Users.query.all()

   result = []

   for user in users:
       user_data = {}
       user_data['public_id'] = user.public_id
       user_data['name'] = user.name
       user_data['password'] = user.password
       user_data['admin'] = user.admin

       result.append(user_data)

   return jsonify({'users': result})

@mod.route('/author', methods=['POST', 'GET'])
@token_required
def create_author(current_user):

   data = request.get_json()

   new_authors = Authors(name=data['name'], country=data['country'], book=data['book'], booker_prize=True, user_id=current_user.id)
   db.session.add(new_authors)
   db.session.commit()

   return jsonify({'message' : 'new author created'})


