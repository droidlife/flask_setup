from api.middleware import auth_required
from flask import request
from api.models import Order


def get(customer_name, customer_email=None):
    payload = {
        'customer_name': customer_name,
        'customer_email': customer_email
    }
    return payload, 200


@auth_required('admin')
def post(order_data):
    order = Order.create(customer_name=order_data['customer_name'], customer_email=order_data['customer_email'])
    order_data['order_id'] = order.id
    return order_data, 200
