from flask import Blueprint, jsonify, request, g
from ecommerce import db
from ecommerce.vendor.model import Vendor
from ecommerce.role.model import Role
from ecommerce.product.model import Product
mod = Blueprint('vendor',__name__,url_prefix='/vendor')

@mod.route('/add_vendor',methods=['POST'])
def add_vendor():
    vendor_name = request.form.get('vendor_name')
    vendor_password = request.form.get('vendor_password')
    vendor_address = request.form.get('vendor_address')
    vendor = Vendor(
        vendor_name = vendor_name,
        vendor_password = vendor_password,
        vendor_address = vendor_address
    )
    role = Role(
        vendor = vendor,
        role_person_name = vendor_name,
        role_password=vendor_password,
        role_name= 'vendor'
    )
    db.session.add(role)
    db.session.add(vendor)
    db.session.commit()
    return "vendor and role details added"

@mod.route('/update_vendor_name/<v_id>',methods=['PUT'])
def update_vendor_name(v_id):
    vendor_name = request.form.get('vendor_name')
    vendor = Vendor.query.get(v_id)
    vendor.vendor_name = vendor_name
    db.session.commit()
    return "updated"

@mod.route('/update_vendor_password/<v_id>',methods=['PUT'])
def update_vendor_password(v_id):
    vendor_password = request.form.get('vendor_password')
    vendor = Vendor.query.get(v_id)
    vendor.vendor_password = vendor_password
    db.session.commit()
    return "updated"

@mod.route('/update_vendor_address/<v_id>',methods=['PUT'])
def update_vendor_address(v_id):
    vendor_address = request.form.get('vendor_address')
    vendor = Vendor.query.get(v_id)
    vendor.vendor_address = vendor_address
    db.session.commit()
    return "updated"

@mod.route('/update_vendor_all/<v_id>',methods=['PUT'])
def update_vendor_all(v_id):
    vendor_address = request.form.get('vendor_address')
    vendor_password = request.form.get('vendor_password')
    vendor_name = request.form.get('vendor_name')
    vendor = Vendor.query.get(v_id)
    vendor.vendor_name = vendor_name
    vendor.vendor_password = vendor_password
    vendor.vendor_address = vendor_address
    db.session.commit()
    return "updated"

@mod.route('/delete_vendor/<v_id>',methods=['DELETE'])
def delete_vendor(v_id):
    vendor = Vendor.query.get(v_id)
    db.session.delete(vendor)
    db.session.commit()
    return "deleted"

@mod.route('/update_product_name/<p_id>',methods=['PUT'])
def update_product_name(p_id):
    product_name = request.form.get('product_name')
    product = Product.query.get(p_id)
    product.product_name = product_name
    db.session.commit()
    return "updated"

@mod.route('/update_product_cost/<p_id>',methods=['PUT'])
def update_product_cost(p_id):
    product_cost = request.form.get('product_cost')
    product = Product.query.get(p_id)
    product.product_name = product_cost
    db.session.commit()
    return "updated"

@mod.route('/update_product_stock/<p_id>',methods=['PUT'])
def update_product_stock(p_id):
    product_avail_stock = request.form.get('product_avail_stock')
    product = Product.query.get(p_id)
    product.product_name = product_avail_stock
    db.session.commit()
    return "updated"

@mod.route('/delete_product/<p_id>',methods=['DELETE'])
def delete_product(p_id):
    product = Product.query.get(p_id)
    db.session.delete(product)
    db.session.commit()
    return "deleted"

@mod.route('/update_product_all/<p_id>',methods=['PUT'])
def update_product_all(p_id):
    product_name = request.form.get('product_name')
    product_cost = request.form.get('product_cost')
    product_avail_stock = request.form.get('product_avail_stock')
    product = Product.query.get(p_id)
    product.product_name = product_name
    product.product_name = product_cost
    product.product_name = product_avail_stock
    db.session.commit()
    return "updated"
