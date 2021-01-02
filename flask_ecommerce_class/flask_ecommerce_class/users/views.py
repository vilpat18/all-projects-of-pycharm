from flask import jsonify, Blueprint, request, g
from flask import current_app as app
from itsdangerous import URLSafeSerializer
from flask_ecommerce_class import db,auth
from flask import session
from flask_ecommerce_class.users.models import User,UserDetails,Address

mod = Blueprint('users',__name__,url_prefix='/users')

@auth.verify_token
def verify_auth_token(token):
    print('----token',token)
    s = URLSafeSerializer(app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except Exception:
        return False
    g.user = User.query.get(data['id'])
    return True

@mod.route('',methods=['GET'])
@auth.login_required
def fetch_users():
    # users = User.query.with_entities(User.username,UserDetails.name).all(), select * from user
    # print((users), users[0].username) #accessing using column name
    users = User.query.all() # select * from user
    response = [users.to_representation() for user in users]
    return jsonify(response) ,200

