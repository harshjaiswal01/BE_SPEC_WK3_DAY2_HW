from database import db #need db be to serve incoming data to db
from models.product import Products #need this to create Product Objects
from sqlalchemy import select, delete, func
from marshmallow import fields, ValidationError
from flask import Flask, jsonify, request
from models.schemas.productSchema import product_schema, products_schema2, products_schema

def add_product(product_data):
    try:
        product_data = product_schema.load(product_data)
    except ValidationError as e:
        return None, jsonify(e.messages)
    
    new_product = Products(product_name = product_data["product_name"], price=product_data["price"])
    db.session.add(new_product)
    db.session.commit()
    return jsonify({"Message":"Product Successfully Added!!!"}), None

def get_products():
    query = select(Products)
    result = db.session.execute(query).scalars() #Execute query and convert row objects into scaler objects (python usable)
    productz = result.all()
    return products_schema.jsonify(productz)

def get_products_paginate(page, per_page):
    query = select(Products)
    productz = db.paginate(query, page=page, per_page=per_page)
    return products_schema.jsonify(productz)

def get_product(id):

    query = select(Products).filter(Products.id == id)
    result = db.session.execute(query).scalars().first()

    if result is None:
        return None, jsonify({"Error":"Product not found"})

    return product_schema.jsonify(result), None

def update_product(id, product_data):

    query = select(Products).where(Products.id == id)
    result = db.session.execute(query).scalars().first()
    # print(result)
    if result is None:
        return None, jsonify({"Error":"Product not Found"})
    
    product = result
    
    try:
        product_data = product_schema.load(product_data)
        print(product_data)
    except ValidationError as e:
        return None, jsonify(e.messages)
    
    for field, value in product_data.items():
        setattr(product, field, value)

    db.session.commit()
    return jsonify({"MEssage" : "Product details have been updated"}), None

def delete_product(id):
    query = delete(Products).filter(Products.id == id)

    result = db.session.execute(query)

    if result.rowcount == 0:
        return None, jsonify({"Error":"Product not found"})
    
    if result is None:
        return None, jsonify({"Error":"Product not found 2"})
    
    db.session.commit()
    return jsonify({"Message":"Successfully removed Product!!!"}), None