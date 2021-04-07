import flask
from app import app
from flask import json, render_template, request, session, Response,jsonify,redirect,url_for,flash,make_response
from app.models import User
from app.forms import forms
from app.database import mysql_db

@app.route('/getalluser',methods=['GET'])
def getAllUser():
    get_part = User.User.query.all()
    part_schema = User.UserSchema(many=True)
    part = part_schema.dump(get_part)
    return make_response(jsonify({"User": part}))

@app.route('/deleteUserbyId', methods = ['GET', 'POST'])
def deleteUserbyId():
    if request.method == 'POST':
        user_id = 1 #testing
        delete_user = User.User.query.filter(User.User.id == user_id).first()
        mysql_db.session.delete(delete_user)
        mysql_db.session.commit()

        return make_response(jsonify({"Delete User": "Success"}))