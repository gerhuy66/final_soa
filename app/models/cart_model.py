from app.database import mysql_db
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema


class Cart(mysql_db.Model):
    __tablename__ = 'carts'
    c_id = mysql_db.Column(mysql_db.String(20), primary_key = True)
    quantity = mysql_db.Column(mysql_db.Integer())
    total_cost = mysql_db.Column(mysql_db.Integer())
    

    def __init__(self,c_id,quantity,total_cost):
        self.c_id = c_ida
        self.quantity = quantity
        self.total_cost = total_cost

    def create(self):
        mysql_db.session.add(self)
        mysql_db.session.commit()
        return self

    def to_json(self):
        return {
            "c_id":self.c_id,
            "quantity":self.quantity,
            "total_cost":self.total_cost
        }

    def __repr__(self):
        return '<Cart %r, %r, %r>' % (self.c_id, self.quantity, self.total_cost)

class StudentSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Cart
        sqla_session = mysql_db.session

    p_id = fields.Number(dump_only=True)
    quantity = fields.String(required=True)
    total_cost = fields.String(required=True)
    
