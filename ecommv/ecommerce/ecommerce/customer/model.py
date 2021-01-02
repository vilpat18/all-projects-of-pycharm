from ecommerce import db
class Customer(db.Model):
    __tablename__='customer'
    customer_id = db.Column('customer_id',db.Integer,primary_key=True,autoincrement=True)
    customer_name = db.Column('customer_name',db.String(20),nullable=False,unique=False)
    customer_password = db.Column('customer_password',db.String(30),nullable=False,unique=True)
    customer_address = db.Column('customer_address',db.String(30),nullable=False,unique=False)
    role_details = db.relationship('Role',backref='customer',uselist=False,lazy='select',cascade='all,delete')
    cart_details = db.relationship('Cart', backref='customer', lazy='select',
                                         uselist=False, cascade='all,delete')

    def to_representation(self):
        return {
            'customer_name': self.customer_name,
            'customer_pwd': self.customer_password,
            'customer_address': self.customer_address,
            'role_details': self.role_details.role_name,
            'cart_details':self.cart_details.to_representation()
        }
