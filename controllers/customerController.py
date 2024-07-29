from services import customerService
from database import db #need db be to serve incoming data to db
from models.customer import Customer #need this to creat Customer Objects
from sqlalchemy import select, delete, func
from marshmallow import fields, ValidationError
from flask import Flask, jsonify, request
from models.schemas.customerSchema import customers_schema, customer_schema
from utils.util import admin_required, token_required

@admin_required
def get_customers():
    print("Getting Customers")
    customerz = customerService.get_customers()
    return customers_schema.jsonify(customerz), 201

@admin_required
def get_customer(id):

    customer, error = customerService.get_customer(id)
    print("Getting One Customer")
    if error:
        return error, 400
    return customer, 201

@token_required
def add_customer():

    try:
        customer_data = customer_schema.load(request.json)
        # print(customer_data)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    customer = customerService.add_customer(customer_data)
    return customer_schema.jsonify(customer), 201

@token_required
def update_existing_customer(id):
    customer_data = request.json
    updated_customer, error = customerService.update_customer_service(id, customer_data)
    
    if error:
        return jsonify(error), 400
    
    return jsonify({"Message": "Customer details have been updated"})

@admin_required
def delete_customer(id):

    delete_customer, error = customerService.delete_customer(id)
    if error:
        return error, 404
    
    return jsonify({"Message":"Successfully removed Customer!!!"}), 201

@admin_required
def find_all_paginate():
    page = int(request.args.get("page"))
    per_page = int(request.args.get("per_page"))
    customers = customerService.find_all_paginate(page, per_page)
    return customers_schema.jsonify(customers), 200

def login():
    try:
        credentials = request.json
        token = customerService.login(credentials['username'], credentials['password'])
    except KeyError:
        return jsonify({'messages': 'Invalid payload, expecting username and password'}), 401
    
    if token:
        return jsonify(token), 200
    else:
        return jsonify({'messages': "Invalid username or password"}), 401