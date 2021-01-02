from bank_flask_app import db

class Customers(db.Model):
    __tablename__='customer'
    cst_id = db.Column('cst_id',db.Integer,primary_key = True,autoincrement=True)
    cust_name = db.Column('cust_name',db.String(50))
    city= db.Column('city',db.String(50))
    bank_id= db.Column('bank_id',db.Integer,db.ForeignKey('bankinfo.bank_id'))
    acc_id = db.Column('acc_id',db.Integer,db.ForeignKey('account.acc_id'))
  # ''' bank = db.relationship("Bankinfo", backref='customer',lazy='select'
    #                          uselist=False,cascade='all,delete')
   # account = db.relationship("Account",secondary='account',backref='customer',
                            #  lazy='joined',cascade='all,delete')'''





    def __repr__(self):
        return {"cst_id":self.cst_id,
                "bank_id":self.bank_id,
                'acc_id':self.acc_id,
                "cust_name":self.cust_name,
                "city":self.city }
