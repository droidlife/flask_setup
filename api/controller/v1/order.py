from api.middleware import auth_required
from flask import request
from api.models import Order
from api.serializer.dto.order_dto import OrderDto
from api.serializer.dao.order_dao import OrderDao


def get(customer_name, customer_email=None):
    order_list = Order.query.filter_by(customer_name=customer_name).all()
    payload = OrderDto(many=True).dump(order_list).data
    result = {
        'order_list': payload
    }
    return result, 200


@auth_required('admin')
def post(order_data):
    result = OrderDao().load(order_data)
    if result.errors:
        return result.errors, 400

    order = Order.create(**result.data)
    order_data['order_id'] = order.id
    return order_data, 200
