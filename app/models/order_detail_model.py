from enum import unique
from app import services
from app.database import mysql_db
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema


class Order_Detail(mysql_db.Model):
    __tablename__ = 'order_detail'
    p_id = mysql_db.Column(mysql_db.String(20), primary_key = True)
    order_id = mysql_db.Column(mysql_db.String(20), primary_key = True)
    shop_id = mysql_db.Column(mysql_db.String(20),primary_key = False)
    status = mysql_db.Column(mysql_db.String(20))
    order_user_email = mysql_db.Column(mysql_db.String(100))

    def __init__(self, p_id,order_id,shop_id,status,order_user_email):
        self.p_id = p_id
        self.order_id = order_id
        self.shop_id = shop_id
        self.status = status
        self.order_user_email = order_user_email

    def create(self):
        mysql_db.session.add(self)
        mysql_db.session.commit()
        return self

    def __repr__(self):
        return '<Order_Detail %r, %r, %r, %r, %r>' % (self.p_id,self.order_id,self.shop_id, self.status, self.order_user_email)

class Order_DetailSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Order_Detail
        sqla_session = mysql_db.session

    p_id = fields.String(dump_only=True)
    order_id = fields.String()
    shop_id = fields.String()
    status = fields.String()
    order_user_email = fields.String()
