from flaskAPI import db

class Users(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    public_id = db.Column(db.Integer)
    name = db.Column(db.String(32))
    password = db.Column(db.String(10))
    admin = db.Column(db.Boolean)

class Authors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique = True, nullable = False)
    book = db.Column(db.String(32), unique = True, nullable = False)
    country = db.Column(db.String(32),nullable = False)
    booker_prize = db.Column(db.Boolean)


    db.create_all()

