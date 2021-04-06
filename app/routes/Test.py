import flask
from marshmallow.fields import Email
from app import app
from flask import json, render_template, request, session, Response,jsonify,redirect,url_for,flash,make_response
from flask_login import login_required,login_user,logout_user,current_user
from app.models import Order, Order_Detail
from app.forms import forms
from app.database import mysql_db
import datetime

@app.route('/test', methods=['GET','POST'])
def test():
    if request.method == "POST":
        products = request.json.get("products")
        return str(len(products))
    return 'method get'
