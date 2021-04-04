import flask
from marshmallow.fields import Email
from app import app
from flask import json, render_template, request, session, Response,jsonify,redirect,url_for,flash,make_response
from flask_login import login_required,login_user,logout_user,current_user
from app.models import User,Product,ProductsSchema,Order,OrderSchema,Order_Detail,Order_DetailSchema
from app.forms import forms
from app.database import mysql_db
from app.services import mailService
import datetime

class order_status:
    WAITING = "wait"
    CONFIMRED = "confirmed"
    SHIPPING = "shipping"
    RECIEVED = "recieved"


@app.route("/order",methods=['GET','POST'])
def doOrder():
    # required data
    # request data valid json construction
    # {
    #   "items":[{
    #   "productId":"p1","shopId":"s1"
    # },
    # {
    #   "productId":"p2","shopId":"s2"
    # }
    # ]
    # } 
    # print(item['productId'])
    # print(item['shopId'])
    ro = request.json['items']
    rp = []
    x = datetime.datetime.now()
    date_time = x.strftime("%H%M%S%d%m%Y")
    status = order_status.WAITING
    new_order = Order(date_time,status,x.strftime("%H:%M:%S-%d/%m/%Y"),current_user.email,10000).create()
    for item in ro:
        new_oder_detail = Order_Detail(item['productId'],new_order.oder_id,item['shopId'],new_order.status,new_order.user_do_oder).create()
        # rp.append({"orderId":new_order.oder_id,"OrderStatus":new_order.status,"shipFee":new_order.ship_fee,"createDate":new_order.create_dt,"shopId":new_oder_detail.shop_id})
    
    return make_response(jsonify({"status":"200","message":"Order Successful"}))



@app.route("/confirmOrder",methods=['POST'])
def confirmOrder():
    # input = {
    #   "order":{
    #     "orderId":"123213",
    #     "productId":"ádsa"
    # }
    # }
    data = request.json['order']
    o_detail = Order_Detail.query.filter_by(order_id=data['orderId'],p_id=data['productId'])
    o_detail.update(dict(status=order_status.CONFIMRED))
    mysql_db.session.commit()

    mailService.sendEmail("TPH market Notification",o_detail.first().order_user_email,"Your product"+data['productId']+" have been Confirmed!")
    return make_response(jsonify({"status":"200","message":"confirm Order Successful"}))

@app.route("/trackingOrderStatus",methods=['POST'])
def trackingOrderStatus():
    data = request.json['order']
    order_id = data['orderId']
    o_d_query = Order_Detail.query.filter_by(order_id=order_id).all()
    o_d_shcema = Order_DetailSchema(many=True)
    o_ds = o_d_shcema.dump(o_d_query)
    return make_response(jsonify({"orderDetail":o_ds}))

