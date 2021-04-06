from flask import Flask, json, render_template, request, session, Response,jsonify,redirect,url_for
from flask_login import LoginManager
app = Flask(__name__,static_url_path='/static')
from flask_bootstrap import Bootstrap
UPLOAD_FOLDER = './uploads'
PRODUCT_UPLOAD_FOLDER = './app/static/images/products'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PRODUCT_UPLOAD_FOLDER'] = PRODUCT_UPLOAD_FOLDER
bootstrap = Bootstrap(app)

from app.routes import views,product_view,order_view,myshop_view,orderWithBanking
from app.models import User,Role
from app.models import product_model,Order,Order_Detail,Shop,Partner,Shipping, Catagory, Location,Shop, Product
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
    return dict(db=mysql_db,Partner = Partner,Shop = Shop, Location = Location,Catagory= Catagory, User = User.User, Role = Role.Role, Product = Product,Shipping = Shipping, Order = Order, Order_Detail = Order_Detail)