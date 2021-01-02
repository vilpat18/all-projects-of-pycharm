from bank_flask_app import db

class Bankinfo(db.Model):
    __table_name__ = 'bank'
    bank_id =db.Column('bank_id',db.Integer,primary_key = True,autoincrement=True)
    bank_name = db.Column('bank_name',db.String(20),)
    bank_state = db.Column('bank_state',db.String(20))
    ifsc_code = db.Column('ifsc_code',db.String(20),unique=True)


    def __repr__(self):
        return {"bank_name":self.bank_name,
                "bank_state":self.bank_state,
                "ifsc_code":self.ifsc_code}










