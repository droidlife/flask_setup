from flask import request


def auth_required(*users):
    def authenticator(func):
        def wrap(*args, **kwargs):
            request.user = users[0]
            return func(*args, **kwargs)
        wrap.__name__ = func.__name__
        return wrap
    return authenticator


def log_request(current_request):
    print(current_request.method, current_request.path, current_request.endpoint, current_request.host_url)
    print(current_request.query_string, current_request.data)
