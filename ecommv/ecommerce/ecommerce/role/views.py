from flask import Blueprint, jsonify, request, g
from ecommerce import db
from ecommerce.role.model import Customer,Role
mod = Blueprint('role',__name__,url_prefix='/role')

# @mod.route('/add_customer',methods=['POST'])
# def add_customer():
#     name = request.form.get('name')
#     pwd = request.form.get('pwd')
#     addr = request.form.get('addr')
#     cust = Customer(
#         c_name = name,
#         c_pwd = pwd,
#         c_address = addr
#     )
#     role = Role(
#         parent = cust,
#         r_name = name,
#         role_name= 'admin'
#     )
#     db.session.add(role)
#     db.session.add(cust)
#     db.session.commit()
#     return "aadede"

