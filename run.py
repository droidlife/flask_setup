from app import create_app
from app.logger import log_data
from flask import request

app = create_app()


@app.app.before_request
def before_request():
    log_data(request)


if __name__ == '__main__':
    app.run(port=8080)
