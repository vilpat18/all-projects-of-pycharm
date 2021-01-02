class config(object):
    SECRET_KEY = 'vilaspatil999'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/firstapp'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopementConfig(config):
    DEBUG =True
    SQLALCHEMY_ECHO = True

class ProductionConfig(config):
    DEBUG = False

app_config = {
               'developement':DevelopementConfig,
                'production': ProductionConfig
             }


