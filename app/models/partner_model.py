from enum import unique
from app.database import mysql_db
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema


class Partner(mysql_db.Model):
    __tablename__ = 'partners'
    partner_id = mysql_db.Column(mysql_db.String(20),primary_key=True)
    user_id = mysql_db.Column(mysql_db.String(64))

    def __init__(self, partner_id,user_id):
        self.partner_id = partner_id
        self.user_id = user_id


    def create(self):
        mysql_db.session.add(self)
        mysql_db.session.commit()
        return self

    def __repr__(self):
        return '<Partner %r, %r>' % (self.partner_id,self.user_id)

class PartnerSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Partner
        sqla_session = mysql_db.session
    partner_id = fields.String(dump_only=True)
    user_id = fields.String()

