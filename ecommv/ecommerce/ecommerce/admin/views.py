from flask import Blueprint, jsonify, request, g
from ecommerce import db
from ecommerce.role.model import Role
from ecommerce.admin.model import Admin
from ecommerce.product.model import ProductCategory,Subcategory,Product
from ecommerce.vendor.model import Vendor
from ecommerce.customer.model import Customer
mod = Blueprint('admin',__name__,url_prefix='/admin')

@mod.route('/add_admin',methods=['POST'])
def add_admin():
    admin_name = request.form.get('admin_name')
    admin_password = request.form.get('admin_password')
    admin_address = request.form.get('admin_address')
    admin = Admin(
        admin_name = admin_name,
        admin_password = admin_password,
        admin_address = admin_address
    )
    role = Role(
        admin = admin,
        role_person_name = admin_name,
        role_password=admin_password,
        role_name= 'admin'
    )
    db.session.add(role)
    db.session.add(admin)
    db.session.commit()
    return "admin and role details added"

@mod.route('/fetch_all_admin',methods=['GET'])
def fetch_all_admin():
    admins = Admin.query.all()
    response = [admin.to_representation() for admin in admins]
    return jsonify(response)

@mod.route('/update_admin_name/<admin_id>',methods=['PUT'])
def update_admin_name(admin_id):
    admin_name = request.form.get('admin_name')
    admin = Admin.query.get(admin_id)
    admin.admin_name = admin_name
    db.session.commit()
    return "updated"

@mod.route('/update_admin_password/<admin_id>',methods=['PUT'])
def update_admin_password(admin_id):
    admin_password = request.form.get('admin_password')
    admin = Admin.query.get(admin_id)
    admin.admin_password = admin_password
    db.session.commit()
    return "updated"

@mod.route('/update_admin_address/<admin_id>',methods=['PUT'])
def update_admin_address(admin_id):
    admin_address = request.form.get('admin_address')
    admin = Admin.query.get(admin_id)
    admin.admin_address = admin_address
    db.session.commit()
    return "updated"

@mod.route('/update_admin_all/<admin_id>',methods=['PUT'])
def update_admin_all(admin_id):
    admin_name = request.form.get('admin_name')
    admin_address = request.form.get('admin_address')
    admin_password = request.form.get('admin_password')
    admin = Admin.query.get(admin_id)
    admin.admin_name = admin_name
    admin.admin_password = admin_password
    admin.admin_address = admin_address
    db.session.commit()
    return "updated"

@mod.route('/delete_admin/<admin_id>',methods=['DELETE'])
def delete_admin(admin_id):
    admin = Admin.query.get(admin_id)
    db.session.delete(admin)
    db.session.commit()
    return "deleted"

@mod.route('/add_product_category',methods=['POST'])
def add_product_category():
    product_category_name = request.form.get('product_category_name')
    product_category = ProductCategory(
        product_category_name = product_category_name
    )
    db.session.add(product_category)
    db.session.commit()
    return "category added"

@mod.route('/add_product_sub_category',methods=["POST"])
def add_product_subcategory():
    product_subcategory_name = request.form.get('product_subcategory_name')
    category = request.form.get('category')
    c_id = ProductCategory.query.filter(ProductCategory.product_category_name==category).first()
    if c_id is None:
        product_category = ProductCategory(
            product_category_name=category
        )
        subcategory = Subcategory(
            product_category=product_category,
            product_subcategory_name=product_subcategory_name
        )
        db.session.add(product_category)
        db.session.add(subcategory)
        db.session.commit()
        return "subcategory and category added"
    else:
        subcategory = Subcategory(
            product_subcategory_name=product_subcategory_name,
            product_subcategory_category_id=int(c_id.product_category_id)
        )
        db.session.add(subcategory)
        db.session.commit()
        return "subcategory added"

@mod.route('/delete_product_category/<category_id>',methods=['DELETE'])
def delete_product_category(category_id):
    category = ProductCategory.query.get(category_id)
    db.session.delete(category)
    db.session.commit()
    return "deleted"

@mod.route('/delete_product_subcategory/<subcategory_id>',methods=['DELETE'])
def delete_product_subcategory(subcategory_id):
    subcategory = Subcategory.query.get(subcategory_id)
    db.session.delete(subcategory)
    db.session.commit()
    return "deleted"

@mod.route('/add_product',methods=['POST'])
def add_product():
    product_name = request.form.get('product_name')
    subcategory = request.form.get('subcategory')
    category = request.form.get('category')
    product_cost = request.form.get('product_cost')
    product_avail_stock=request.form.get('product_avail_stock')
    vendor_name = request.form.get('vendor_name')
    is_category = ProductCategory.query.filter(ProductCategory.product_category_name == category).first()
    is_subcategory = Subcategory.query.filter(Subcategory.product_subcategory_name == subcategory).first()
    v_id = Vendor.query.filter(Vendor.vendor_name == vendor_name).first()
    if is_category is None and is_subcategory is None:
        product_category = ProductCategory(
            product_category_name=category
        )
        subcategory = Subcategory(
            product_category=product_category,
            product_subcategory_name=subcategory
        )
        product=Product(
            product_category = subcategory,
            product_name = product_name,
            product_cost = product_cost,
            product_avail_stock = product_avail_stock,
            product_vendor_id = int(v_id.vendor_id)
        )
        db.session.add(product_category)
        db.session.add(subcategory)
        db.session.add(product)
        db.session.commit()
        return "product and c,s added"
    elif is_category is not None and is_subcategory is None:
        subcategory = Subcategory(
            product_subcategory_name=subcategory,
            product_subcategory_category_id =int(is_category.product_category_id)
        )
        product = Product(
            product_category=subcategory,
            product_name=product_name,
            product_cost=product_cost,
            product_avail_stock=product_avail_stock,
            product_vendor_id=int(v_id.vendor_id)
        )
        db.session.add(subcategory)
        db.session.add(product)
        db.session.commit()
        return "product and s added"
    else:
        product = Product(
            product_name=product_name,
            product_subcategory_id=int(is_subcategory.product_subcategory_id),
            product_cost=product_cost,
            product_avail_stock=product_avail_stock,
            product_vendor_id=int(v_id.vendor_id)
        )
        db.session.add(product)
        db.session.commit()
        return "product added"

@mod.route('/fetch_all_customer',methods=['GET'])
def fetch_all_customer():
    customers = Customer.query.all()
    response = [customer.to_representation() for customer in customers]
    return jsonify(response)

@mod.route('/fetch_customer_by_name',methods=['GET'])
def fetch_customer_by_name():
    customer_name = request.form.get('customer_name')
    customers = Customer.query.filter(Customer.customer_name == customer_name)
    customer = [x.to_representation() for x in customers]
    return jsonify(customer)

@mod.route('/fetch_all_vendor',methods=['GET'])
def fetch_all_vendor():
    vendors = Vendor.query.all()
    response = [vendor.to_representation() for vendor in vendors]
    return jsonify(response)

@mod.route('/fetch_vendor_by_name',methods=['GET'])
def fetch_vendor_by_name():
    vendor_name = request.form.get('vendor_name')
    vendors = Vendor.query.filter(Vendor.vendor_name == vendor_name)
    vendor = [x.to_representation() for x in vendors]
    return jsonify(vendor)