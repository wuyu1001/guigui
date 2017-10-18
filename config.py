class Config(object):
    DEBUG = False
    TESTING = False

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
