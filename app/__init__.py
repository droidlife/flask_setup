import connexion
from app.config import app_config


def create_app():
    app = connexion.FlaskApp(__name__, instance_relative_config=True, swagger_ui=False)
    app.app.config.from_object(app_config['development'])
    app.add_api('swagger.yml')
    app.debug = True
    return app
