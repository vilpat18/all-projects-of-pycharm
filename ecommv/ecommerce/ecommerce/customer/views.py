from flask import Blueprint, jsonify, request, g
from ecommerce import db
from ecommerce.customer.model import Customer
from ecommerce.role.model import Role
mod = Blueprint('customer',__name__,url_prefix='/customer')

@mod.route('/add_customer',methods=['POST'])
def add_customer():
    customer_name = request.form.get('customer_name')
    customer_password = request.form.get('customer_password')
    customer_address = request.form.get('customer_address')
    customer = Customer(
        customer_name = customer_name,
        customer_password = customer_password,
        customer_address = customer_address
    )
    role = Role(
        customer = customer,
        role_person_name = customer_name,
        role_password=customer_password,
        role_name= 'customer'
    )
    db.session.add(role)
    db.session.add(customer)
    db.session.commit()
    return "customer and role details added"

@mod.route('/update_customer_name/<cust_id>',methods=['PUT'])
def update_customer_name(cust_id):
    customer_name = request.form.get('customer_name')
    customer = Customer.query.get(cust_id)
    customer.customer_name = customer_name
    db.session.commit()
    return "updated"

@mod.route('/update_customer_password/<cust_id>',methods=['PUT'])
def update_customer_password(cust_id):
    customer_password = request.form.get('customer_password')
    customer = Customer.query.get(cust_id)
    customer.customer_password = customer_password
    db.session.commit()
    return "updated"

@mod.route('/update_customer_address/<cust_id>',methods=['PUT'])
def update_customer_address(cust_id):
    customer_address = request.form.get('customer_address')
    customer = Customer.query.get(cust_id)
    customer.customer_address = customer_address
    db.session.commit()
    return "updated"

@mod.route('/delete_customer/<cust_id>',methods=['DELETE'])
def delete_customer(cust_id):
    customer = Customer.query.get(cust_id)
    db.session.delete(customer)
    db.session.commit()
    return "deleted"

@mod.route('/update_customer_all/<cust_id>',methods=['PUT'])
def update_customer_all(cust_id):
    customer_name = request.form.get('customer_name')
    customer_password = request.form.get('customer_password')
    customer_address = request.form.get('customer_address')
    customer = Customer.query.get(cust_id)
    customer.customer_name = customer_name
    customer.customer_password = customer_password
    customer.customer_address = customer_address
    db.session.commit()
    return "updated"