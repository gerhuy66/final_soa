from operator import imod
from app.database import mysql_db
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema
from app.models import model

class Shipping(mysql_db.Model):
    __tablename__ = 'shippings'
    shop_id = mysql_db.Column(mysql_db.String(20), primary_key = True)
    product_id = mysql_db.Column(mysql_db.String(20), primary_key = True)
    create_date = mysql_db.Column(mysql_db.String(30))
    cost = mysql_db.Column(mysql_db.Integer())

    def __init__(self, shop_id,product_id,cost):
        self.shop_id = shop_id
        self.product_id = product_id
        self.cost = cost

    def create(self):
        mysql_db.session.add(self)
        mysql_db.session.commit()
        return self

    def __repr__(self):
        return '<Shipping %r, %r, %r, %r>' % (self.shop_id,self.product_id,self.create_date,self.cost)

class ShippingSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Shipping
        sqla_session = mysql_db.session

    shop_id = fields.String(dump_only=True)
    product_id = fields.String()
    create_date = fields.String()
    cost = fields.Integer()