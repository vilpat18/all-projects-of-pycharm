from flask import Blueprint,jsonify,request,g
from flask import current_app as app
from flask import session
from flask_practice import db, auth
from itsdangerous import URLSafeSerializer
import sqlalchemy.dialects.sqlite
from flask_practice.users.models import User,UserDetails,Address

mod = Blueprint('users',__name__,url_prefix='/users')

@auth.verify_token
def verify_auth_token(token):
    print('_____token',token)
    s = URLSafeSerializer(app.config['SECRET_KEY'])
    try:
        data=s.loads(token)
        print(data)
    except Exception:
        return False
    g.user = User.query.get(data['id'])
    return True

@mod.route('', methods=['GET'])
@auth.login_required
def fetch_users():
    # users = User.query.with_entities(User.username, UserDetails.name).all()  # select * from user;
    # print(users), users[0].username)  # access using column name
    users = User.query.all()  # select * from user;
    # # Without representation
    # print(users[0].username)
    # print(users[0].email)
    # With represtation
    response = [user.to_representation() for user in users]
    return jsonify(response), 200

@mod.route('/get_user/<user_id>',methods=['GET'])
def get_user_by_id(user_id):
    users = User.query.get(int(user_id))
    response =users.to_representation()
    #response.pop('password')
    return jsonify(response),200

@mod.route('/get_user',methods=['GET'])
def fetch_user_by_username():
    username = request.args.get('username')
    user =User.query.filter(User.username==username).first()
    response = user.to_representation()
    return jsonify(response)

'''@mod.route('/get_user',methods=['GET'])
def fetch_by_email():
    email = request.args.get('email')
    user = User.query.filter(User.email==email).first()
    response = user.to_representation
    return jsonify(response)'''

@mod.route('/create_user',methods=['POST'])
def create_user():
    request_data = request.get_json()
    user = User(
        username=request_data['username'],
        email = request_data['email'],
        password = request_data['password'] )
    db.session.add(user)
    db.session.commit()
    return 'user has been created'

@mod.route('/user_update/<user_id>',methods=['PUT'])
def update_user(user_id):
    request_data=request.get_json()
    user = User.query.get(int(user_id))
    user.username = request_data['username']
    #user.email=request_data['email']
    #user.password=request_data['password']
    db.session.commit()
    return "user has been updated"

@mod.route('/add_user_detalis',methods=['POST'])
def add_user_details():
    request_data = request.get_json()
    user_details = UserDetails(name=request_data['name'],
                              user_id= request_data['user_id'] )
    db.session.add(user_details)
    db.session.commit()
    return 'user details has been uploaded'

@mod.route('/fetch_user_details',methods=['GET'])
def fetch_user_details():
    user_details = UserDetails.query.all()
    response = [user_details.to_representation() for user_details in user_details]
    return jsonify(response)

@mod.route('/add_address', methods=['POST'])
def add_address():
    request_data = request.get_json()
    user_id = request_data['user_id']
    address = Address(
        city=request_data['city']
    )
    user = User.query.get(user_id)
    user.addresses.append(address)  # Add to association table
    # user.addressess.delete(address)  # delete from association table
    # db.session.add(address)
    db.session.commit()
    return 'Address detail has been added.'

@mod.route('fetch_addresses',methods=['GET'])
def fetch_addresses():
    addresses= Address.query.all()
    response = [address.to_representation() for address in addresses]
    return jsonify(response)

@mod.route('/login',methods=['POST'])
def login():
    request_data = request.get_json()
    username = request_data['username']
    password = request_data['password']
    user = User.query.filter(User.username==username and User.password==password).first()
    token = user.generate_auth_token()
    response = token
    return jsonify(response),200

@mod.route('/set_cookie',methods=['POST'])
def set_cookie():
    request_data = request.get_json()
    cookie_value = request_data['cookie_value']
    response = jsonify({'msg':'cookie value has been set.'})
    response.set_cookie('my_cookie',cookie_value)

@mod.route('/get_cookies',methods=['GET'])
def get_cookies():
    cookie_value =request.cookies.get('my_cookie')
    return jsonify({'cookie':cookie_value})

@mod.route('/handle_session',methods=['POST','GET'])
def handle_session():
    if request.method == 'POST':
        request_data = request.get_json()
        session_value = request_data['session_value']
        session['my_session']=session_value
        return jsonify({'msg':'session value has been set.'})
    elif request.method == 'GET':
        session_value = session.get('my_session')
        return jsonify({'session':session_value})

@mod.route('/upload_file',methods=['POST'])
def upload_file():
    f =request.files['my_file']
    f.save('docs/'+ f.filename)
    return 'file uploaded'



















