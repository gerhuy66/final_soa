from re import S
from app.database import mysql_db
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema


class Order(mysql_db.Model):
    __tablename__ = 'orders'
    order_id = mysql_db.Column(mysql_db.String(20), primary_key = True)
    status_shipping = mysql_db.Column(mysql_db.String(20))
    status_payment = mysql_db.Column(mysql_db.String(20)
    create_dt = mysql_db.Column(mysql_db.String(100))
    user_do_order = mysql_db.Column(mysql_db.String(20))
    ship_fee = mysql_db.Column(mysql_db.Float())
    total_product = mysql_db.Column(mysql_db.Float())

    def __init__(self, order_id, status_shipping, status_payment, create_dt, user_do_order, ship_fee, total_product):
        self.order_id = order_id

        self.status_shipping = status_shipping
        self.status_payment = status_payment

        self.create_dt =create_dt
        self.user_do_order = user_do_order

        self.ship_fee = ship_fee
        self.total_product = total_product

    def create(self):
        mysql_db.session.add(self)
        mysql_db.session.commit()
        return self

    def to_json(self):
        return {
            "order_id":self.order_id,

            "status_shipping":self.status_shipping,
            "status_payment":self.status_payment,
            "create_dt":self.create_dt,
            "user_do_order":self.user_do_order,

            "ship_fee":self.ship_fee,
            "total_product":self.total_product,
        }

    def __repr__(self):
        return '<Order %r, %r, %r, %r, %r, %r, %r>' % (self.order_id, self.status_shipping, self.status_payment, self.create_dt,self.user_do_order,self.ship_fee,self.total_product)

class OrderSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Order
        sqla_session = mysql_db.session

    order_id = fields.String(dump_only=True)

    status_shipping = fields.String(required=False)
    status_payment = fields.String(required=False)
    create_dt = fields.String(required=False)
    user_do_order = fields.String(required=False)

    ship_fee = fields.Float(required=False)
    total_product = fields.Float()
    
