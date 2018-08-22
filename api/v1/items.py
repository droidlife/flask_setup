def get(message, name=None):
    print(name)
    return {"one": message}, 200


def post(message):
    print(message)
    return {}, 200


def v1_get(message, name=None):
    print(message)
    print(name)

    return {"message": message, "name": name}, 200
