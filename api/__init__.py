from functools import wraps
from flask import g, request


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        print(request.headers)
        request.user = 11
        return f(*args, **kwargs)

    return decorated_function
