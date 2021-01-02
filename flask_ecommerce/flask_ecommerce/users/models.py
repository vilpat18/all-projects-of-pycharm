from flask_ecommerce import db

class user3(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name =db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(20))
    location = db.Column(db.String(100))
    dept = db.Column(db.String(20))
    mob = db.Column(db.Integer)

    def __repr__(self):
        return {
                "first_name":self.first_name,
                "last_name":self.last_name,
                "emai":self.email,
                "password":self.password,
                "location":self.location,
                "dept":self.dept,
                 "mob":self.mob }


from itsdangerous import URLSafeSerializer

from flask_ecommerce import db
from flask import current_app as app, g

users_addresses = db.Table('users_addresses',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('address_id', db.Integer, db.ForeignKey('address.id'), primary_key=True)
)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement = True)
    username = db.Column('username', db.String(64), index=True, unique=True)
    email = db.Column('email', db.String(120), unique=True)
    password = db.Column('password', db.String(128))
    user_detail = db.relationship('UserDetails', backref='user', lazy=True, uselist=False, cascade="all,delete",
                                  ) # one-to-one relationship
    addresses = db.relationship('Address', secondary=users_addresses, backref='user', lazy='joined' #use 'dynamic' and check the difference
                                , cascade="all,delete"
                                 ) # Many-to-many Relationship

    def to_representation(self):
        if self.user_detail:
            user_detail = self.user_detail.to_representation()
        else:
            user_detail = {}
        addresses = [x.to_representation() for x in self.addresses]
        return {
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'user_detail': user_detail,
            'addresses': addresses
        }

    def generate_auth_token(self):
        s = URLSafeSerializer(app.config['SECRET_KEY'])
        return s.dumps({'id': self.id})


class UserDetails(db.Model):
    __tablename__ = 'user_details'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement = True)
    name = db.Column('name', db.String(64), nullable=True)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('user.id'), nullable=False)

    def to_representation(self):
        return {
            'name': self.name
        }

class Address(db.Model):
    __tablename__ = 'address'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement = True)
    city = db.Column('city', db.String(64), nullable=True)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('user.id'), nullable=False)

    def to_representation(self):
        return {
            'city': self.city
        }



