from flask import request, jsonify
from services import customerService #dont import the individual function, import the module as a whole
from marshmallow import ValidationError, fields
from . import ma

class OrderSchema(ma.Schema):
    id = fields.Integer(required=False)
    order_date = fields.Date(required=False)
    customer_id = fields.Integer(required=True)
    expected_delivery_date = fields.Date(required=False)
    products = fields.Nested("ProductSchema", many=True)
    customer = fields.Nested("CustomerOrderSchema")

    class Meta:
        fields = ("id", "order_Date", "customer_id", "expected_delivery_date", "items") #Items will be a list of product_ids

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)