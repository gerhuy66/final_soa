import flask
from marshmallow.fields import Email
from app import app
from flask import json, render_template, request, session, Response,jsonify,redirect,url_for,flash,make_response
from flask_login import login_required,login_user,logout_user,current_user
from app.models import Order, Order_Detail
from app.forms import forms

@app.route('/orderwithbanking', methods=['GET','POST'])
def orderWithBanking():
    inputOrder = {
	"products":[
	{"p_id":"ip14","shop_id":"shop1","p_name":"iphone 14","product_des":"best phone ever"},
	{"p_id":"ip15","shop_id":"shop1","p_name":"iphone 15","product_des":"best phone ever"},
	],
	"totalCost":"9990000",
	"status":"paid",
	"paymentDatetime":"01042021",
	"paymentUser":"duchuy1096@gmail.com",
	"paymentId":"pay01042021huy"
}
    if request.method == 'POST':
        return make_response(jsonify({"status":200, "message":"order completed"}))
    return 'test'

    return 'method get'

