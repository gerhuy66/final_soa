from app.database import mysql_db
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema


class Catagory(mysql_db.Model):
    __tablename__ = 'catagories'
    id = mysql_db.Column(mysql_db.String(20), primary_key = True)
    catagory_code = mysql_db.Column(mysql_db.String(20))
    catagory_name = mysql_db.Column(mysql_db.String(50))
    catagory_des = mysql_db.Column(mysql_db.String(100))

    def __init__(self,catagory_code,catagory_name,catagory_des):
        self.catagory_code = catagory_code
        self.catagory_name = catagory_name
        self.catagory_des = catagory_des

    def create(self):
        mysql_db.session.add(self)
        mysql_db.session.commit()
        return self

    def to_json(self):
        return {

        }

    def __repr__(self):
        return '<Catagory %r, %r, %r>' % (self.catagory_code, self.catagory_name, self.catagory_des)

class CatagorySchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Catagory
        sqla_session = mysql_db.session

    id = fields.String(dump_only=True)
    catagory_code = fields.String()
    catagory_name = fields.String()
    catagory_des = fields.String()