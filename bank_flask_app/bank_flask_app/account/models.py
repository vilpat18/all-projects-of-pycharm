from bank_flask_app import db

class Account(db.Model):
    __table_name__ = 'account'
    acc_id = db.Column('acc_id',db.Integer, primary_key=True, autoincrement=True)
    acc_number = db.Column('acc_number',db.Integer , unique=True)
    acc_balance = db.Column('acc_balance',db.Integer, nullable=True)


    def __repr__(self):
        return {
                "acc_number":self.acc_number,
                "acc_balance":self.acc_balance
                                                }



