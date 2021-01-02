from ecommerce import db
from ecommerce.product.model import Product
from ecommerce.customer.model import Customer
from ecommerce.admin.model import PaymentType
class Cart(db.Model):
    __tablename__ = 'cart'
    cart_id = db.Column('cart_id', db.Integer, primary_key=True, autoincrement=True)
    cart_product_id = db.Column('cart_product_id',db.Integer,db.ForeignKey('product.product_id'),unique=False,nullable=False)
    cart_quantity_to_buy = db.Column('cart_quantity_to_buy', db.Integer, unique=False, nullable=False)
    cart_customer_id = db.Column('cart_customer_id', db.Integer, db.ForeignKey('customer.customer_id'), unique=False,nullable=False)
    cart_total_price = db.Column('cart_total_price',db.Integer,nullable=False)
    def to_representation(self):
        product = Product.query.get(self.cart_product_id)
        customer = Customer.query.get(self.cart_customer_id)
        return{
            'cart_product_id':self.cart_product_id,
            'cart_quantity_to_buy':self.cart_quantity_to_buy,
            'cart_customer_id':self.cart_customer_id,
            'total_price':self.cart_total_price,
            'product_name':product.product_name,
            'customer_name':customer.customer_name
        }

class Wishlist(db.Model):
    __tablename__ = 'wishlist'
    wishlist_id = db.Column('cart_id', db.Integer, primary_key=True, autoincrement=True)
    wishlist_product_id = db.Column('wishlist_product_id',db.Integer,db.ForeignKey('product.product_id'),unique=False,nullable=False)
    wishlist_quantity_to_buy = db.Column('wishlist_quantity_to_buy', db.Integer, unique=False, nullable=False)
    wishlist_customer_id = db.Column('wishlist_customer_id', db.Integer, db.ForeignKey('customer.customer_id'), unique=False,nullable=False)
    wishlist_total_price = db.Column('wishlist_total_price', db.Integer, nullable=False)
    def to_representation(self):
        return{
            'cart_product_id':self.wishlist_product_id,
            'cart_quantity_to_buy':self.wishlist_quantity_to_buy,
            'cart_customer_id':self.wishlist_customer_id,
            'total_price':self.wishlist_total_price
        }
class Myorders(db.Model):
    __tablename__ = 'myorders'
    myorders_id = db.Column('myorders.id', db.Integer, primary_key=True, autoincrement=True)
    myorders_quantity=db.Column('myorders_quantity',db.Integer,nullable=False)
    myorders_product_id = db.Column('myorders_product_id',db.Integer,db.ForeignKey('product.product_id'),nullable=False)
    myorders_customer_id = db.Column('myorders_customer_id', db.Integer, db.ForeignKey('customer.customer_id'),nullable=False)
    myorders_payment_type_id = db.Column('myorders_payment_type_id', db.Integer, db.ForeignKey('payment_type.p_method_id'),nullable=False)
    order_date = db.Column('order_date',db.String(20),nullable=False)
    myorders_total_price = db.Column('myorders_total_price', db.Integer, nullable=False)
    def to_representation(self):
        product = Product.query.get(self.myorders_product_id)
        customer = Customer.query.get(self.myorders_customer_id)
        payment =PaymentType.query.get(self.myorders_payment_type_id)
        return {
            'quantity':self.myorders_quantity,
            'product':product.product_name,
            'customer':customer.customer_name,
            'total_price':self.myorders_total_price,
            'date':self.order_date,
            'paymen_type': payment.p_method_name
        }