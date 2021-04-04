from app.database import mysql_db
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema


class Location(mysql_db.Model):
    __tablename__ = 'locations'
    loc_code = mysql_db.Column(mysql_db.String(20),primary_key = True)
    loc_name = mysql_db.Column(mysql_db.String(50))
    loc_des = mysql_db.Column(mysql_db.String(100))

    def __init__(self,loc_code,loc_name,loc_des):
        self.loc_code = loc_code
        self.loc_name = loc_name
        self.loc_des = loc_des

    def create(self):
        mysql_db.session.add(self)
        mysql_db.session.commit()
        return self

    def to_json(self):
        return {

        }

    def __repr__(self):
        return '<Location %r, %r, %r>' % (self.loc_code, self.loc_name, self.loc_des)

class LocationSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Location
        sqla_session = mysql_db.session
    loc_code = fields.String()
    loc_name = fields.String()
    loc_des = fields.String()