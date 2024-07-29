from flask import request, jsonify
from services import customerService #dont import the individual function, import the module as a whole
from marshmallow import ValidationError, fields
from . import ma

class ProductSchema(ma.Schema):
    id = fields.Integer(required = False)
    product_name = fields.String(required = True)
    price = fields.Float(required = True)

    class Meta:
        fields = ("id", "product_name", "price")

class ProductSchema1(ma.Schema):
    id = fields.Integer(required = False)
    product_name = fields.String(required = True)
    price = fields.Float(required = True)
    order_date = fields.Date(required = True)

    class Meta:
        fields = ("id", "product_name", "price", "order_date")

class ProductTrackSchema(ma.Schema):
    id = fields.Integer(required = False)
    product_name = fields.String(required = True)
    price = fields.Float(required = True)
    expected_delivery_date = fields.Date(required = True)

    class Meta:
        fields = ("id", "product_name", "price", "expected_delivery_date")

product_schema = ProductSchema()
products_schema = ProductSchema(many = True)

products_schema2 = ProductSchema1(many = True)

track_schema = ProductTrackSchema()