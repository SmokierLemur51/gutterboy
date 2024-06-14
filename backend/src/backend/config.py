import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    # change to quart databases 
    """
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://{}:{}@{}:5432/{}".format(
            os.environ["DB_USERNAME"],
            os.environ['DB_PASSWORD'],
            os.environ['DB_HOST'],
            os.environ['DATABASE_NAME'],
        )
    """
    QUART_DB_DATABASE_URL = "postgresql://{}:{}@{}:5432/{}".format(
            os.environ["PG_USERNAME"],
            os.environ['PG_PASSWORD'],
            os.environ['PG_HOST'],
            os.environ['PG_DATABASE'],
        )
    # SQLALCHEMY_DATABASE_URI="sqlite:///{}.db".format(os.environ['SQLITE_DB_FILE'])


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
