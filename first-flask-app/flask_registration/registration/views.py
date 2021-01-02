from flask import Blueprint,jsonify ,request
from flask_registration import db
from flask_registration.registration.models import User

mod = Blueprint('registration',__name__,url_prefix='/registration')

@mod.route('',methods = ['POST'])
def new_user():
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        return 'missing fields'
    if User.query.filter_by(username=username).first() is not None:
        return  'user already exsists'
    user = User(username=username)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'username':user.username}),201,{'Location': url_for('get_user',id = user.id,_external= True)}
