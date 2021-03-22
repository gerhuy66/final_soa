from flask import Flask, json, render_template, request, session, Response,jsonify,redirect,url_for
from flask_login import LoginManager
app = Flask(__name__,static_url_path='/static')
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap(app)

from app.routes import views
from app.models import User,Role,Tution,Student,His,cart_model,order_model,product_model
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.User.query.filter_by(id=user_id).first()

from app.database import mysql_db
mysql_db.create_all()


@app.shell_context_processor
def make_shell_context():
    return dict(db=mysql_db, User=User.User,Student = Student.Student, His = His.His)