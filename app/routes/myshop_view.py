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


@app.route("/myshop",methods=['GET'])
def myshop():
   return render_template("myshop.html")