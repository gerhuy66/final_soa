import flask
from app import app
from flask import json, render_template, request, session, Response,jsonify,redirect,url_for,flash,make_response
from app.models import Role, User
from app.forms import forms
from app.database import mysql_db

@app.route('/updaterole',methods=['GET', 'POST'])
def updaterole():
    input = {  
    "id": 1, 
	"role_value": 1
}
    if request.method == 'POST':
        user_id = request.json.get('id')
        role_value = request.json.get("role_value")

        role_user = User.User.query.filter_by(id = user_id)
        role_user.update(dict(role_value = role_value))
        mysql_db.session.commit()
        
        return make_response(jsonify({"status":200, "Update Role": 'Done'}))
    
    return 'method get'
