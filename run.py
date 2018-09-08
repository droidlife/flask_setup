from app import create_app
from api.middleware import log_request
from flask import request


app = create_app()
flask_app = app.app


@flask_app.before_request
def before_request():
    log_request(request)


if __name__ == '__main__':
    app.run(port=8080)
