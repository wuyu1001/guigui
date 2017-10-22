import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    


    # Put any configurations here that are common across all environments

class ProductionConfig(Config):

    DEBUG = False
    SECRET_KEY = 'p9Bv<3Eid9%$i01' 
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

class DevelopmentConfig(Config):
    DEBUG = True
    SQLACHEMY_ECHO = True

class TestingConfig(Config):
    TESTING = True


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
