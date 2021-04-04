from enum import unique
from app.database import mysql_db
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema
import datetime

class Shop(mysql_db.Model):
    __tablename__ = 'shops'
    
    shop_id = mysql_db.Column(mysql_db.String(20), primary_key = True)
    owner_id = mysql_db.Column(mysql_db.String(64),unique=True)
    shop_name = mysql_db.Column(mysql_db.String(100))
    create_date = mysql_db.Column(mysql_db.String(100))

    def __init__(self,owner_id,shop_name,create_date):
        now  = datetime.datetime.now()
        self.shop_id ="pro"+now.strftime("%H%M%S%m%d%Y")
        self.owner_id = owner_id
        self.shop_name = shop_name
        self.create_date = create_date

    def create(self):
        mysql_db.session.add(self)
        mysql_db.session.commit()
        return self

    def __repr__(self):
        return '<Shop %r, %r, %r, %r>' % (self.shop_id,self.owner_id,self.shop_name,self.create_date)

class ShopSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Shop
        sqla_session = mysql_db.session

    shop_id = fields.String(dump_only=True)
    owner_id = fields.String()
    shop_name = fields.String()
    create_date = fields.String()
