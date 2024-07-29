from services import productService
from database import db #need db be to serve incoming data to db
from models.customer import Customer #need this to creat Customer Objects
from sqlalchemy import select, delete, func
from marshmallow import fields, ValidationError
from flask import Flask, jsonify, request
from models.schemas.productSchema import product_schema, products_schema
from utils.util import admin_required, token_required

@admin_required
def add_product():
    product_data = request.json
    new_product, error = productService.add_product(product_data)

    if error:
        return error, 400
    
    return new_product, 201

def get_products():
    productz = productService.get_products()
    return productz, 201

def get_products_paginate():
    page = int(request.args.get("page"))
    per_page = int(request.args.get("per_page"))
    productz = productService.get_products_paginate(page, per_page)
    return productz, 200

def get_product(id):
    product, error = productService.get_product(id)
    if error:
        return error, 400

    return product, 201

@admin_required
def update_product(id):
    product_data = request.json
    updated_product, error = productService.update_product(id, product_data)

    if error:
        return error, 400
    
    return updated_product, 201

@admin_required
def delete_product(id):
    deletion, error = productService.delete_product(id)

    if error:
        return error, 400
    return deletion, 201