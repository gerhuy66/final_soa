from app.database import mysql_db
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema
import datetime

class Model(mysql_db.Model):
    __tablename__ = 'models'
    
    id = mysql_db.Column(mysql_db.String(20),primary_key = True)
    create_date = mysql_db.Column(mysql_db.String(100))

    def __init__(self,create_date):
        x = datetime.datetime.now()
        self.create_date = x.strftime("%H%M%S%d%m%Y")
    
    def create(self):
        mysql_db.session.add(self)
        mysql_db.session.commit()
        return self

class Shipping(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Model
        sqla_session = mysql_db.session

    id = fields.String(dump_only=True)
    create_date = fields.String()
