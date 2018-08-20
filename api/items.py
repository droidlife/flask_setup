def get(message, name=None):
    print(name)
    return {"one": message}, 200


def post(message):
    print(message)
    return {}, 200
