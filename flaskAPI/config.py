class Config(object):
    SECRET_KEY = 'vilpat123456'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/flaskapi'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    DEBUG = False

app_config = {
         "development":DevelopmentConfig,
         "production": ProductionConfig
}