from api import login_required
from flask import request


def get(message, name=None):
    print(name)
    return {"one": message}, 200


@login_required
def post(message):
    print(request.user)
    print(message)
    return {}, 200
