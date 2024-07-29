from flask import Blueprint
from controllers.orderController import add_order, order_items, order_tracking, get_order_paginated

order_blueprint = Blueprint('order_bp', __name__)

order_blueprint.route('/', methods=['POST'])(add_order)
order_blueprint.route('/<int:id>', methods=['GET'])(order_items)
order_blueprint.route('/track/<int:id>', methods=['GET'])(order_tracking)
order_blueprint.route('/p', methods=['GET'])(get_order_paginated)