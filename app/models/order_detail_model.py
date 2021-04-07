from enum import unique
from app import services
from app.database import mysql_db
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema
import datetime


class Order_Detail(mysql_db.Model):
    __tablename__ = 'order_detail'
    p_id = mysql_db.Column(mysql_db.String(20), primary_key = True)
    order_id = mysql_db.Column(mysql_db.String(20), primary_key = True)
    shop_id = mysql_db.Column(mysql_db.String(20),primary_key = False)
    amount = mysql_db.Column(mysql_db.Integer())
    status_shipping = mysql_db.Column(mysql_db.String(20), server_default = 'wait')
    order_user_email = mysql_db.Column(mysql_db.String(100))
    ibanking_payment_email = mysql_db.Column(mysql_db.String(100), server_default = 'COD') #thanh toán ibanking thì lưu mail, mặc định là COD: thu tiền tiền mặt
    paymentId = mysql_db.Column(mysql_db.String(100))

    def __init__(self, p_id, shop_id, amount, status_shipping, order_user_email, ibanking_payment_email, paymentId):
        self.p_id = p_id
        self.shop_id = shop_id
        self.amount = amount
        self.status_shipping = status_shipping
        self.order_user_email = order_user_email
        self.ibanking_payment_email = ibanking_payment_email
        self.paymentId = paymentId

    def create(self):
        now = datetime.datetime.now()
        self.order_id = "order" + now.strftime("%H%M%S%d%m%Y")
        mysql_db.session.add(self)
        mysql_db.session.commit()
        return self

    def to_json(self):
        return {
            "p_id":self.p_id,
            "order_id":self.order_id,
            "shop_id":self.shop_id,
            "amount":self.amount,
            "status_shipping":self.status_shipping,
            "ibanking_payment_email":self.status_payment,
            "paymentId":self.paymentId,
        }

    def __repr__(self):
        return '<Order_Detail %r, %r, %r, %r, %r, %r, %r, %r>' % (self.p_id, self.order_id, self.shop_id, self.amount, self.status_shipping, self.order_user_email, self.ibanking_payment_email, self.paymentId)

class Order_DetailSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Order_Detail
        sqla_session = mysql_db.session

    p_id = fields.String(dump_only=True)
    order_id = fields.String()
    shop_id = fields.String()
    amount = fields.Integer()
    status_shipping = fields.String()
    order_user_email = fields.String()
    ibanking_payment_email = fields.String()
    paymentId = fields.String()
