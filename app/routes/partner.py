import flask
from app import app
from flask import json, render_template, request, session, Response,jsonify,redirect,url_for,flash,make_response
from app.models import partner_model
from app.forms import forms
from app.database import mysql_db

@app.route('/partnerById/<partner_id>',methods=['GET','POST'])
def getPartnerById(partner_id):
    get_partid = partner_model.Partner.query.filter(partner_model.Partner.partner_id == partner_id).firt()
    partid_schema = partner_model.PartnerSchema(many=True)
    partid = partid_schema.dump(get_partid)
    return make_response(jsonify({"PartnerID": partid}))

@app.route('/getallpartner',methods=['GET','POST'])
def getAllPartner():
    get_part = partner_model.Partner.query.all()
    part_schema = partner_model.PartnerSchema(many=True)
    part = part_schema.dump(get_part)
    return make_response(jsonify({"Partner": part}))

@app.route('/approveid',methods=['GET','POST'])
def approve_id():
    partner_id = request.json['partnerId']
    part_query = partner_model.Partner.query.filter(partner_model.Partner.partner_id == partner_id)
    part = part_query.first()
    part_query.update(dict(status="Approved"))
    return make_response(jsonify({"Status": "Success"}))
