import connexion
from app.config import app_config
from app.constant import SERVER, DB_CONNECTION_URL
from api.models import db, ma
from flask_migrate import Migrate


def create_app():
    app = connexion.FlaskApp(__name__, instance_relative_config=True, swagger_ui=False)
    app.app.config.from_object(app_config[SERVER])

    app.app.config['SQLALCHEMY_DATABASE_URI'] = DB_CONNECTION_URL
    app.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.add_api('route.yaml')

    if SERVER == 'development':
        app.debug = True

    db.init_app(app.app)
    ma.init_app(app.app)
    Migrate(app.app, db, compare_type=True)

    return app
