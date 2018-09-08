from api.middleware import auth_required
from flask import request
from api.models import Order, Comment
from api.serializer.dto import OrderDto
from api.serializer.dao import OrderDao


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

    order = Order.create(customer_name=result.data['customer_name'], customer_email=result.data['customer_email'])

    comment_list = []
    for comment in result.data['comments']:
        comment_list.append(Comment(text=comment, order_id=order.id))

    Comment.bulk_create(comment_list)

    return order_data, 200
