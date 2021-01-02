from bank_flask_app import db

class Transaction(db.Model):
    __tablename__ = 'transaction'
    trans_id = db.Column('trans_id',db.Integer,primary_key=True,autoincrement=True)
    cst_id_from = db.Column('cst_id_from',db.Integer,db.ForeignKey('customer.cst_id_from'))
    cst_id_to = db.Column('cst_id_to',db.Integer,db.ForeignKey('customer.cst_id_to'))
    amount = db.Column('amount',db.Integer)
    acc_type = db.Column('acc_type',db.String(10))
