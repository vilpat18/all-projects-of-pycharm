class config(object):
    SECRET_KEY ='vilas999'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/bank_app'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class developmentconfig(config):
    DEBUG = True
    SQLALCHEMY_ECHO =True

class productionconfig(config):
    DEBUG = False

app_config ={"development":developmentconfig,
             "production":productionconfig}


