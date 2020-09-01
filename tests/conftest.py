import time

import pytest
from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists, drop_database
from testing.postgresql import Postgresql

from api import create_app
from api.config import TestingConfig
from api.models.base import db


@pytest.fixture(scope="session")
def postgres():
    """
    Postgres fixture - starts a postgres instance inside a temp directory
    and closes it after tests are done
    """
    with Postgresql() as postgresql:
        yield postgresql
        postgresql.stop()


@pytest.fixture(scope="session")
def client(postgres):
    """
    Postgres client instance
    """
    engine = create_engine(TestingConfig.SQLALCHEMY_DATABASE_URI)
    if not database_exists(engine.url):
        create_database(engine.url)

    app = create_app(TestingConfig)
    app.app_context().push()

    db.create_all()
    client = app.test_client()
    yield client
    db.session.close()
    db.drop_all()
    drop_database(engine.url)
