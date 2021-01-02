class Config(object):
    SECRET_KEY='vilas999'
    SQLALCHEMY_DATABASE_URI='mysql://root:root@localhost/practice_db'
    SQLALCHEMY_TRACK_MODIFICATIONS =False

class Development_config(Config):
    '''
    developement configuration
    '''
    DEBUG=True
    SQLALCHEMY_ECHO=True

class Production_config(Config):
    '''
    production configuration
    '''
    DEBUG=False

class Testing_config(Config):
    '''
       testing configuration
     '''
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/practice_db'
    SQLALCHEMY_ECHO=True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app_config={'Development':Development_config,
            'Testing':Testing_config,
            'Production':Production_config}