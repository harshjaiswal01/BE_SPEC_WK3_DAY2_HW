from flask import Blueprint
from controllers.productController import add_product, get_product, get_products, update_product, delete_product, get_products_paginate

product_blueprint = Blueprint('product_bp', __name__)

product_blueprint.route('/', methods=['POST'])(add_product)
product_blueprint.route('/', methods=['GET'])(get_products)
product_blueprint.route('/p', methods=['GET'])(get_products_paginate)
product_blueprint.route('/<int:id>', methods=['GET'])(get_product)
product_blueprint.route('/<int:id>', methods=['PUT'])(update_product)
product_blueprint.route('/<int:id>', methods=['DELETE'])(delete_product)