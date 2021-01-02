from itsdangerous import URLSafeSerializer

from ecommerce import db, auth
from flask import current_app as app, g
from ecommerce.vendor.model import Vendor
class ProductCategory(db.Model):
    __tablename__ = 'product_category'
    product_category_id = db.Column('product_category_id',db.Integer,primary_key=True,autoincrement=True)
    product_category_name = db.Column('product_category_name',db.String(20),nullable=False,unique=True,index=True)
    product_detail = db.relationship('Subcategory',backref='product_category',lazy='select',
                                     uselist=True,cascade = 'all,delete')
    def to_representation(self):
        if self.product_detail:
            prod_detail = [x.to_representation() for x in self.product_detail]
        else:
            prod_detail = {}
        return {
            'product_category_name':self.product_category_name,
            'product_detail':prod_detail
        }

class Subcategory(db.Model):
    __tablename__ = 'product_subcategory'
    product_subcategory_id = db.Column('product_subcategory_id',db.Integer,primary_key=True,autoincrement=True)
    product_subcategory_name = db.Column('product_subcategory_name',db.String(20),index=True,nullable=False,unique=True)
    product_subcategory_category_id = db.Column('product_subcategory_category_id',db.Integer,db.ForeignKey('product_category.product_category_id'),nullable=False,unique=False)
    sub_product_detail = db.relationship('Product',backref='product_category',lazy='select',
                                         uselist=True,cascade='all,delete')
    def to_representation(self):
        if self.sub_product_detail:
            sub_prod_detail=[x.to_representation() for x in self.sub_product_detail]
        else:
            sub_prod_detail = {}
        return {
            'product_subcategory_name':self.product_subcategory_name,
            'sub_prod_detail':sub_prod_detail
        }

class Product(db.Model):
    __tablename__='product'
    product_id=db.Column('product_id',db.Integer,primary_key=True,autoincrement=True)
    product_name = db.Column('product_name',db.String(100),unique=False,index=True,nullable=False)
    product_subcategory_id = db.Column('product_subcategory_id',db.Integer,db.ForeignKey('product_subcategory.product_subcategory_id'),nullable=False)
    product_cost = db.Column('product_cost',db.Integer,unique=False,nullable=False)
    product_avail_stock = db.Column('product_avail_stock',db.Integer,unique=False,nullable=False)
    product_vendor_id = db.Column('product_vendor_id',db.Integer,db.ForeignKey('vendor.vendor_id'),unique=False,nullable=False)
    cart_details = db.relationship('Cart', backref='product', lazy='select',
                                         uselist=True, cascade='all,delete')
    wishlist_details = db.relationship('Wishlist', backref='product', lazy='select',
                                   uselist=True, cascade='all,delete')
    def to_representation(self):
        if self.cart_details:
            cart = [x.to_representation() for x in self.cart_details]
        else:
            cart = {}
        if self.wishlist_details:
            wishlist = [x.to_representation() for x in self.wishlist_details]
        return {
            'p_name':self.product_name,
            'p_cost':self.product_cost,
            'p_avail_stock':self.product_avail_stock,
            'cart_details':cart,
            'wishlist_details':wishlist
        }