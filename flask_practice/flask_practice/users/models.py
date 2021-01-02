from itsdangerous import URLSafeSerializer
from flask_practice import db,auth
from flask import current_app as app, g

users_addresses = db.Table('users_addresses',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('address_id', db.Integer, db.ForeignKey('address.id'), primary_key=True)
)

class User(db.Model):
    __tablename__='user'
    id = db.Column('id',db.Integer, primary_key=True ,autoincrement =True)
    username=db.Column('username',db.String(50),index=True,unique=True)
    email=db.Column('email',db.String(50),unique=True)
    password=db.Column('password',db.String(50))

    user_details= db.relationship('UserDetails',backref='user',lazy='select',
                                  uselist=False,cascade='all,delete') #one to one relationship

    addresses = db.relationship('Address',secondary=users_addresses,backref='user',
                                lazy='joined',cascade='all,delete')
    #inplace of 'joined' use 'dynamic' and see the difference

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
        return s.dumps({'id':self.id})

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
    __tablename__= 'address'
    id = db.Column('id',db.Integer,primary_key=True,autoincrement=True)
    city = db.Column('city',db.String(20),nullable=True)

    def to_representation(self):
        return {'city':self.city}







