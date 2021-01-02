from flask import Blueprint,jsonify,request,g
from flask import Blueprint, jsonify, request, g
from flask import current_app as app
from flask import session
from itsdangerous import URLSafeSerializer
from ecommerce import db, auth
from ecommerce.product.model import ProductCategory, Subcategory, Product
mod = Blueprint('product',__name__,url_prefix='/product')
@mod.route('/fetch_all_category_product',methods=['GET'])
def fetch_all_category_product():
    categories = ProductCategory.query.all()
    response = [category.to_representation() for category in categories]
    return jsonify(response)

@mod.route('/fetch_product_by_name',methods=['GET'])
def fetch_product_by_name():
    p_name = request.form.get('p_name')
    products = Product.query.filter(Product.p_name == p_name)
    product = [x.to_representation() for x in products]
    return jsonify(product)

@mod.route('/fetch_product_by_subcategory',methods=['GET'])
def fetch_product_by_subcategory():
    s_name = request.form.get('s_name')
    s_product = Subcategory.query.filter(Subcategory.s_name == s_name).first()
    return jsonify(s_product.to_representation())

@mod.route('/fetch_product_category_name',methods=['GET'])
def fetch_product_by_category_name():
    c_name = request.form.get('c_name')
    c_product = ProductCategory.query.filter(ProductCategory.c_name == c_name).first()
    return jsonify(c_product.to_representation())
@mod.route('/fetch_all_product',methods=['GET'])
def fetch_all_product():
    products = Product.query.all()
    product = [x.to_representation() for x in products]
    return jsonify(product)