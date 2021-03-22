from re import S
from app.database import mysql_db
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema


class Order(mysql_db.Model):
    __tablename__ = 'orders'
    oder_id = mysql_db.Column(mysql_db.String(20), primary_key = True)
    p_id = mysql_db.Column(mysql_db.String(20))
    status = mysql_db.Column(mysql_db.String(20))
    create_dt = mysql_db.Column(mysql_db.String(20))
    user_do_oder = mysql_db.Column(mysql_db.String(20))
    shop_id = mysql_db.Column(mysql_db.String(20))
    ship_fee = mysql_db.Column(mysql_db.Integer())

    def __init__(self,order_id,p_id,status,create_dt,user_do_oder,shop_id,ship_fee):
        self.oder_id = order_id
        self.p_id = p_id
        self.status = status
        self.create_dt =create_dt
        self.user_do_oder = user_do_oder
        self.shop_id = shop_id
        self.ship_fee = ship_fee


    def create(self):
        mysql_db.session.add(self)
        mysql_db.session.commit()
        return self

    def to_json(self):
        return {
            "oder_id":self.oder_id,
            "p_id":self.p_id,
            "status":self.status,
            "create_dt":self.create_dt,
            "user_do_oder":self.user_do_oder,
            "shop_id":self.shop_id,
            "ship_fee":self.ship_fee,
        }

    def __repr__(self):
        return '<Cart %r, %r, %r>' % (self.c_id, self.quantity, self.total_cost)

class StudentSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Order
        sqla_session = mysql_db.session

    oder_id = fields.String(dump_only=True)
    p_id = fields.String(required=False)
    status = fields.String(required=False)
    create_dt = fields.String(required=False)
    user_do_oder = fields.String(required=False)
    shop_id = fields.String(required=False)
    ship_fee = fields.String(required=False)
    
