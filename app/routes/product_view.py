import flask
from marshmallow.fields import Email
from app import app
from flask import json, render_template, request, session, Response,jsonify,redirect,url_for,flash,make_response
from flask_login import login_required,login_user,logout_user,current_user
from app.models import User,Product,ProductsSchema
from app.forms import forms

@app.route("/products")
def all_product():
    get_products = Product.query.all()
    product_sche =  ProductsSchema(many=True)
    products = product_sche.dump(get_products)
    return make_response(jsonify({"products_info":products}))

@app.route("/products/<product_id>")
def product_detail(product_id):
    get_products = Product.query.filter_by(p_id = product_id).first()
    product_sche =  ProductsSchema(many=False)
    products = product_sche.dump(get_products)
    return make_response(jsonify({"products_info":products}))

