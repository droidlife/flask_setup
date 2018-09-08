from api.middleware import auth_required
from flask import request


def get(customer_name, customer_email=None):
    payload = {
        'customer_name': customer_name,
        'customer_email': customer_email
    }
    return payload, 200


@auth_required('admin')
def post(order_data):
    print(order_data)
    print(request.user)
    return order_data, 200
