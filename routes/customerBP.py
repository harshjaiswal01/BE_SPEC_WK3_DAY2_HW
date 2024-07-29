from flask import Blueprint
from controllers.customerController import get_customer, get_customers, add_customer, update_existing_customer, delete_customer, find_all_paginate, login

customer_blueprint = Blueprint('customer_bp', __name__)

customer_blueprint.route("/<int:id>", methods = ["GET"])(get_customer)
customer_blueprint.route("/", methods = ["GET"])(get_customers)
customer_blueprint.route('/', methods=['POST'])(add_customer)
customer_blueprint.route('/<int:id>', methods=['PUT'])(update_existing_customer)
customer_blueprint.route('/<int:id>', methods=['DELETE'])(delete_customer)
customer_blueprint.route("/p", methods = ["GET"])(find_all_paginate)
customer_blueprint.route('/login', methods=['POST'])(login)