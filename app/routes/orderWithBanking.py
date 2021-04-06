import flask
from marshmallow.fields import Email
from app import app
from flask import json, render_template, request, session, Response,jsonify,redirect,url_for,flash,make_response
from flask_login import login_required,login_user,logout_user,current_user
from app.models import Order, Order_Detail
from app.forms import forms
from app.database import mysql_db
import datetime

@app.route('/orderwithbanking', methods=['GET','POST'])
def orderWithBanking():
    Order_paid_banking = {
    "status":"paid",
	"products":[
	{"p_id":"ip14","shop_id":"shop1"},
	{"p_id":"ip15","shop_id":"shop1"},
	],
    "order_user_email":"duchuy1096@gmail.com",
    "ibanking_payment_email":"duchuy1096@gmail.com",
    'ship_fee': 20000,
	"total_product": 9990000,

}
    if request.method == 'POST':
        

        if Order_paid_banking['status'] == 'paid': 
            time_order = datetime.datetime.now()
            date_time = time_order.strftime("%H%M%S%d%m%Y")

            #add order table
            order = Order(order_id = date_time, status = 'wait', create_dt = time_order, user_do_order = Order_paid_banking['order_user_email'], ship_fee = Order_paid_banking['ship_fee'], total_product = Order_paid_banking['total_product'])
            mysql_db.session.add(order)
            mysql_db.session.commit()

            #add order_detail table
            for item in Order_paid_banking['products']:
                order_detail = Order_Detail(p_id = item['p_id'], order_id = date_time, shop_id = item['shop_id'], status = 'wait', order_user_email = Order_paid_banking['order_user_email'], ibanking_payment_email = Order_paid_banking['ibanking_payment_email'])
                mysql_db.session.add(order_detail)
                mysql_db.session.commit()

            return make_response(jsonify({"status":200, "message":"order completed", 'time_order':time_order, 'time': date_time}))

        return 'not paid'

    return 'method get'

