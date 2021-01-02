from flask_registration import db
from passlib.apps import custom_app_context as pwd_context

class User(db.Model):
    __table_name__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(32),index=True)
    password_hash = db.Column(db.String(10))

    def hash_password(self,password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self,password):
        return pwd_context.verify(password,self.password_hash)

