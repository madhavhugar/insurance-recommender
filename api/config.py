from os import environ


class Config:
    """
    Base configuration
    """
    # db
    user = environ.get('POSTGRES_USER')
    password = environ.get('POSTGRES_PASSWORD')
    host = environ.get('POSTGRES_HOST')
    db = environ.get('POSTGRES_DB')
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{user}:{password}@{host}/{db}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # flask-jwt
    SECRET_KEY = environ.get('JWT_SECRET_KEY')
    JWT_AUTH_URL_RULE = '/auth/login'

    DEBUG = False
    TESTING = False


class TestingConfig(Config):
    """
    Testing configuration
    """
    TESTING = True

    user = environ.get('POSTGRES_USER')
    password = environ.get('POSTGRES_PASSWORD')
    host = environ.get('POSTGRES_HOST')
    db = 'test'
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{user}:{password}@{host}/{db}'
