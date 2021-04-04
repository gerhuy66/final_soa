from flask.wrappers import Request
from app.models.product_model import ProductSchema
import flask
from flask.signals import request_started
from marshmallow.fields import Email, Method
from app import app
from flask import json, render_template, request, session, Response,jsonify,redirect,url_for,flash,make_response
from flask_login import login_required,login_user,logout_user,current_user
from app.models import User,Product,ProductsSchema
from app.forms import forms
import datetime
x = datetime.datetime.now()
date_time = x.strftime("%H%M%S%d%m%Y")


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

@app.route("/uploadProductFile",methods=['POST'])
def uploadProductFile():
    file = request.files['productImage']
    file.save(os.path.join(app.config['PRODUCT_UPLOAD_FOLDER'], file.filename))
    return make_response(jsonify({"status":200,"uploadSuccess":"1"}))

# @app.route("/createProduct")
# def create_product():
#     data = request.get_json()
#     product_schema = ProductSchema()
#     product = product_schema.load(data)
#     rs = product_schema.dump(product.create()) 
#     return make_response(jsonify({"status":"200","message":"createSuccess","product":rs}))


@app.route("/createProduct",methods=['POST'])
def createProduct():
    product_data = request.get_json()
    # p_name = product_data['pname']
    # p_price = product_data['price']
    # p_des = product_data['des']
    # p_loc = product_data['loc']
    # catagory = product_data['catagory']
    # shop_id = product_data['shopId']
    # Product(p_name,p_price,p_des,p_loc,catagory_code=catagory,img_url="",shop_id = shop_id).create()
    return make_response(jsonify({"status":200,"message":"create successfull","dateTime":date_time}))


import os
import pandas as pd
@app.route("/uploadProductFile",methods = ['GET','POST'])
def importProducts():
    if request.method == 'POST':
        file = request.files['products_file']
        print(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    return render_template('upload_products.html')

from xlrd import open_workbook
@app.route("/readExel")
def readExel():
    wb = open_workbook('uploads/products.xls')
    products = []
    for s in wb.sheets():
        for row in range(1,s.nrows):
            newProduct = Product(s.cell(row,0).value)
            for col in range(s.ncols):
                # print(s.cell(row,col).value)
                value = s.cell(row,col).value
                if col == 1:
                    newProduct.p_name = value
                if col == 2:
                    newProduct.p_description = value
                if col == 3:
                    newProduct.p_price = value
                if col == 4:
                    newProduct.p_location = value
            newProduct.create()
            products.append({"product":newProduct.to_json()})
                    
    return make_response(jsonify({"status":200,"message":"import product success","products":products}))