from database import db #need db be to serve incoming data to db
from models.customer import Customer #need this to creat Customer Objects
from sqlalchemy import select, delete, func
from marshmallow import fields, ValidationError
from flask import Flask, jsonify, request
from models.schemas.customerSchema import customers_schema, customer_schema
from utils.util import encode_token

def get_customers():
    query = select(Customer)
    result = db.session.execute(query).scalars() #Execute query and convert row objects into scaler objects (python usable)
    customerz = result.all()
    return customerz

def find_all_paginate(page, per_page):
    query =select(Customer)
    customers = db.paginate(query, page=page, per_page=per_page)
    print("Customers: ",customers)
    return customers

def get_customer(id):
    print("Getting One")

    query = select(Customer).filter(Customer.id == id)
    result = db.session.execute(query).scalars().first()

    if result is None:
        return None, jsonify({"Error":"Customer not found"})

    return customer_schema.jsonify(result), None

def add_customer(customer_data):
    
    new_customer = Customer(customer_name = customer_data["customer_name"], email = customer_data["email"], phone = customer_data["phone"])
    print(new_customer)
    db.session.add(new_customer)
    db.session.commit()

    # return jsonify({"Message":"New Customer Added Successfully"}), 201
    return new_customer


def update_customer_service(id, customer_data):
    query = select(Customer).where(Customer.id == id)
    result = db.session.execute(query).scalars().first()
    
    if result is None:
        return None, {"Error": "Customer not Found"}
    
    customer = result
    
    try:
        validated_data = customer_schema.load(customer_data)
    except ValidationError as e:
        return None, e.messages
    
    for field, value in validated_data.items():
        setattr(customer, field, value)
    
    db.session.commit()
    return customer, None


def delete_customer(id):
    query = delete(Customer).filter(Customer.id == id)

    result = db.session.execute(query)

    if result.rowcount == 0:
        return None, jsonify({"Error":"Customer not found"})
    
    db.session.commit()
    return jsonify({"Message":"Successfully removed Customer!!!"}), None

def login(username, password): #Login using unique info so we dont query multiple users
    query =select(Customer).where(Customer.username == username) 
    customer = db.session.execute(query).scalar_one_or_none() #Query customer table for a cuastomer with the passwed in username

    if customer and customer.password == password: #if we have a customer associated with the username, validate the password
        auth_token = encode_token(customer.id, customer.role.role_name)

        response = {
            "status": "success",
            "message": "Successfully Logged In",
            "auth_token": auth_token
        }
        return response