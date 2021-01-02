from ecommerce import db
from ecommerce.admin.model import Admin
from ecommerce.customer.model import Customer
from ecommerce.vendor.model import Vendor
class Role(db.Model):
    __tablename__ = 'role'
    role_id = db.Column('role_id',db.Integer, primary_key=True, autoincrement=True)
    role_person_name = db.Column('role_person_name', db.String(20), nullable=False, unique=False)
    role_password = db.Column('role_password', db.String(20), nullable=False)
    role_name = db.Column('role_name', db.String(20), nullable=False, unique=False)
    admin_foreign_id = db.Column('admin_foreign_id', db.Integer,db.ForeignKey('admin.admin_id'),nullable=True, unique=True)
    customer_foreign_id = db.Column('customer_foreign_id', db.Integer,db.ForeignKey('customer.customer_id'),nullable=True,unique=True)
    vendor_foreign_id = db.Column('vendor_foreign_id', db.Integer, db.ForeignKey('vendor.vendor_id'),nullable=True,unique=True)
    def to_representation(self):
        return {
            'role_person_name':self.role_person_name,
            'role_password':self.role_password,
            'role_name':self.role_name
        }