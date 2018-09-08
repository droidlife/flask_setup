from api.middleware import auth_required
from flask import request
from api.models import Order
from api.serializer import OrderSerializer


def get(customer_name, customer_email=None):
    order_list = Order.query.filter_by(customer_name=customer_name).all()
    payload = OrderSerializer(many=True).dump(order_list).data
    result = {
        'order_list': payload
    }
    return result, 200


@auth_required('admin')
def post(order_data):
    # order = Order.create(customer_name=order_data['customer_name'], customer_email=order_data['customer_email'])
    # order_data['order_id'] = order.id
    return order_data, 200
