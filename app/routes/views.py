import flask
from marshmallow.fields import Email
from app import app
from flask import json, render_template, request, session, Response,jsonify,redirect,url_for,flash,make_response
from flask_login import login_required,login_user,logout_user,current_user
from app.models import User
from app.forms import forms

@app.route("/",methods=['GET','POST'])
@login_required
def index():
    return render_template('home.html',current_user =current_user)


@app.route("/login",methods=['GET','POST'])
def login():
    form = forms.LoginForm()
    method = request.method
    if method == 'POST':
        user = User.User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify(form.password.data):
            login_user(user, form.remember_me.data)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('index')
            return redirect(next)
        flash('Invalid username or password.')
    return render_template('login.html', form=form)

@app.route("/about")
@login_required
def about():
    return "All about Flask"

@app.route("/tution")
@login_required
def tutioion():
    return render_template("tution.html")

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))



@app.route("/getUsers",methods=['GET'])
def getUsr():
    get_users = User.User.query.all()
    user_schema = User.UserSchema(many=True)
    users = user_schema.dump(get_users)
    return make_response(jsonify({"users": users}))



@app.route("/createUsers",methods=['POST'])
def createUsr():
    data = request.get_json()
    user_schema = User.UserSchema()
    user = user_schema.load(data)
    rs = user_schema.dump(user.create())
    return make_response(jsonify({"user": rs}),201)



    
