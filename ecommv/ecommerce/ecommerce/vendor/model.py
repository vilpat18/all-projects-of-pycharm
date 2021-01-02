from ecommerce import db
class Vendor(db.Model):
    __tablename__='vendor'
    vendor_id = db.Column('vendor_id',db.Integer,primary_key=True,autoincrement=True)
    vendor_name = db.Column('vendor_name',db.String(20),nullable=False,unique=False)
    vendor_password = db.Column('vendor_password',db.String(30),nullable=False,unique=True)
    vendor_address = db.Column('vendor_address',db.String(30),nullable=False,unique=False)
    role_details = db.relationship('Role',backref='vendor',uselist=False,lazy='select',cascade='all,delete')
    product_details = db.relationship('Product', backref='vendor', uselist=True, lazy='select', cascade='all,delete')

    def to_representation(self):
        products = [x.to_representation() for x in self.product_details]
        return {
            'customer_name': self.vendor_name,
            'customer_pwd': self.vendor_password,
            'customer_address': self.vendor_address,
            'role_details': self.role_details.role_name,
            'products':products
        }
