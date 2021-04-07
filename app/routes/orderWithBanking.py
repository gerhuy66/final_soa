import flask
from marshmallow.fields import Email
from app import app
from flask import json, render_template, request, session, Response,jsonify,redirect,url_for,flash,make_response
from flask_login import login_required,login_user,logout_user,current_user
from app.models import Order, Order_Detail
from app.forms import forms
from app.database import mysql_db
import datetime
import requests
@app.route('/orderwithbanking', methods=['GET','POST'])
def orderWithBanking():
    Order_paid_banking = {
    "status_payment":"paid",
	"products":[
	{"p_id":"ip14","shop_id":"shop1", 'amount': 1},
    {"p_id":"ip15","shop_id":"shop1", 'amount': 2}
	],
    "user_do_order":"duchuy1096@gmail.com",
    "ibanking_payment_email":"duchuy1096@gmail.com",
    'ship_fee': 20000,
	"total_product": 9990000,

}
    if request.method == 'POST':

        data = requests.get('http://flask-env.eba-82cahqav.us-east-2.elasticbeanstalk.com/checkPayment/123213?fbclid=IwAR3ALTatAjoG1NThjjKYwuwo7nURoJG4bqeyE46uJjtvEAKD1k7MvmpL5Hg').text
        checkpayment = json.loads(data)
        checkpayment['paymentStatus'] = 'paid'
        if 'unpaid' in checkpayment['paymentStatus']:
            return make_response(jsonify({"status":200, "messCode":"Fail", "message":"Chưa thanh toán!"}))

        else:
            status_payment = request.json.get("status_payment")
            user_do_order = request.json.get("user_do_order")
            ship_fee = request.json.get("ship_fee")
            products = request.json.get("products")
            total_product = request.json.get("total_product")
            products = request.json.get("products")
            p_id = request.json.get("p_id")
            ibanking_payment_email = request.json.get("ibanking_payment_email")
            #add order table
            order = Order(status_shipping = 'wait', status_payment = status_payment, user_do_order = user_do_order, ship_fee = ship_fee, total_product = total_product).create()

            #add order_detail table
            for item in products:
                order_detail = Order_Detail(p_id = item['p_id'], shop_id = item['shop_id'], amount = item['amount'], status_shipping = 'wait', order_user_email = user_do_order, ibanking_payment_email = ibanking_payment_email).create()

            return make_response(jsonify({"status":200, "messCode":"Success", "message":"Order thành công"}))

        

    return 'method GET'

                    
            

