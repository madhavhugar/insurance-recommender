from flask import Flask
from flask_jwt import JWT
from sqlalchemy_utils import create_database, database_exists

from api.config import Config
from api.views.insurance.routes import insurance
from api.views.auth.routes import auth
from api.models.base import db
from api.jwt import authenticate, identity
from api.models.questionnare import Questionnare


app = Flask(__name__)


def create_app(config: Config) -> Flask:
    """
    Flask application factory
    """
    # configuration
    app.config.from_object(config)

    # register blueprints
    app.register_blueprint(auth)
    app.register_blueprint(insurance)

    # auth
    JWT(app, authenticate, identity)

    # database
    db_url = app.config['SQLALCHEMY_DATABASE_URI']
    if not database_exists(db_url):
        create_database(db_url)

    db.init_app(app)
    with app.app_context():
        db.create_all()
        db.session.commit()
    return app


@app.teardown_appcontext
def shutdown_session(exception=None) -> None:
    db.session.remove()
