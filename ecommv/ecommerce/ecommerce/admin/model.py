from ecommerce import db
class Admin(db.Model):
    __tablename__ = 'admin'
    admin_id = db.Column('admin_id',db.Integer,primary_key=True, autoincrement=True)
    admin_name = db.Column('admin_name', db.String(20), nullable=False, unique=False)
    admin_password = db.Column('admin_password', db.String(30), nullable=False, unique=True)
    admin_address = db.Column('admin_address', db.String(30), nullable=False, unique=False)
    role_detail = db.relationship('Role', backref='admin', lazy='select', uselist=False, cascade='all,delete')

    def to_representation(self):
        return {
            'admin_name':self.admin_name,
            'admin_pwd':self.admin_password,
            'admin_address':self.admin_address,
            'role_detail':self.role_detail.role_name
        }

class PaymentType(db.Model):
    __tablename__='payment_type'
    p_method_id = db.Column('p_method_id',db.Integer,primary_key=True, autoincrement=True)
    p_method_name = db.Column('p_method_name', db.String(50), nullable=False, unique=True)
    order_detail = db.relationship('Myorders', backref='payment_type', lazy='select', uselist=True, cascade='all,delete')
    def to_representation(self):
        return {
            'payment_type':self.p_method_name
        }
