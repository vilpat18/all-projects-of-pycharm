class config(object):
    SECRET_KEY = "vilas999"
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/flask_ecom'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Developmentconfig(config):
    DEBUG = True
    SQLALCHEMY_ECHO =True

class productionconfig(config):
    DEBUG = False

app_config ={"development":Developmentconfig,

             "production":productionconfig }
