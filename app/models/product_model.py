from app.database import mysql_db
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema


class Product(mysql_db.Model):
    __tablename__ = 'products'
    p_id = mysql_db.Column(mysql_db.String(20), primary_key = True)
    p_name = mysql_db.Column(mysql_db.String(20))
    p_price = mysql_db.Column(mysql_db.Integer)
    p_description = mysql_db.Column(mysql_db.String(500))
    p_location = mysql_db.Column(mysql_db.String(50))
    c_id = mysql_db.Column(mysql_db.String(20))
    img_url = mysql_db.Column(mysql_db.String(100))

    def __init__(self, p_id, p_name="", p_price=0, p_description="", p_location = "",c_id="",img_url=""):
        self.p_id = p_id
        self.p_name = p_name
        self.p_price = p_price
        self.p_description = p_description
        self.p_location = p_location
        self.c_id = c_id

    def create(self):
        mysql_db.session.add(self)
        mysql_db.session.commit()
        return self

    def to_json(self):
        return {
            "p_id":self.p_id,
            "p_name":self.p_name,
            "p_price":self.p_price,
            "p_description":self.p_description,
            "p_location":self.p_location,
            "c_id":self.c_id,
            "img_url": self.img_url
        }

    def __repr__(self):
        return '<Product %r, %r, %r, %r, %r, %r, %r>' % (self.p_id, self.p_name, self.p_price, self.p_description, self.p_location,self.c_id,self.img_url)

class ProductSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Product
        sqla_session = mysql_db.session

    p_id = fields.String(dump_only=True)
    p_name = fields.String(required=False)
    p_price = fields.String(required=False)
    p_description = fields.String(required=False)
    p_location = fields.String(required=False)
    c_id = fields.String(required=False)
    img_url = fields.String(required=False)
