import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'p9Bv<3Eid9%' 
    SQLALCHEMY_DATABASE_URI = "postgres://uxpkphioqlwoar:ba591c7d0ede8127587ccf9625df5ac571b986e6abd71e1be9139769bd7420d6@ec2-54-163-237-25.compute-1.amazonaws.com:5432/d3rqgtu4j5pc6c"
    


    # Put any configurations here that are common across all environments

class ProductionConfig(Config):

    DEBUG = False
    
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
