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
	"products":[
	{"productId":"p1","shopId":"shop1","productName":"iphone12","product_des":"best phone ever", "amount": 1},
	{"productId":"p2","shopId":"shop1","productName":"iphone13","product_des":"best phone ever", "amount": 2},
	],
	"totalCost":9990000,
	"status":"paid",
	"paymentDatetime":"01042021",
    "userDoOrder": "duchuy1096@gmail.com",
    "shipFee": 20000,
	"paymentUser":"duchuy1096@gmail.com",
	"paymentId":"pay01042021huy"
}
    if request.method == 'POST':

        data = requests.get('http://flask-env.eba-82cahqav.us-east-2.elasticbeanstalk.com/checkPayment/123213?fbclid=IwAR3ALTatAjoG1NThjjKYwuwo7nURoJG4bqeyE46uJjtvEAKD1k7MvmpL5Hg').text
        checkpayment = json.loads(data)
        checkpayment['paymentStatus'] = 'paid'
        if 'unpaid' in checkpayment['paymentStatus']:
            return make_response(jsonify({"status":200, "messCode":"Fail", "message":"Chưa thanh toán!"}))

        else:
            status_payment = checkpayment['paymentStatus']
            paymentId = checkpayment['paymentId']
            user_do_order = request.json.get("userDoOrder")
            ship_fee = request.json.get("shipFee")
            products = request.json.get("products")
            total_product = request.json.get("totalCost")
            ibanking_payment_email = request.json.get("paymentUser")

            #add order table
            order = Order(status_shipping = 'wait', status_payment = status_payment, user_do_order = user_do_order, ship_fee = ship_fee, total_product = total_product).create()

            #add order_detail table
            for item in products:
                order_detail = Order_Detail(p_id = item['productId'], shop_id = item['shopId'], amount = item['amount'], status_shipping = 'wait', order_user_email = user_do_order, ibanking_payment_email = ibanking_payment_email, paymentId = paymentId).create()

            return make_response(jsonify({"status":200, "messCode":"Success", "message":"Order thành công"}))

        

    return 'method GET'

                    
            

