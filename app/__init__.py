import connexion
from app.config import app_config
from app.constant import SERVER


def create_app():
    app = connexion.FlaskApp(__name__, instance_relative_config=True, swagger_ui=False)
    app.app.config.from_object(app_config[SERVER])
    app.add_api('route.yaml')
    if SERVER == 'development':
        app.debug = True
    return app
