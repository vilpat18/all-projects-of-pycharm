
class Config(object):
    """
     common configuration
    """
    # put any configuration here that are common across all envirnoments
    SECRET_KEY = 'vilaspatil999'
    # SQLALCHEMY_DATABASE_URI = '<use_database>://<username>:<password>@<ip>/<database_name>'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/amazon_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopementConfig(Config):
    """
    DevelopmentConfigurations
      """
    DEBUG = True
    SQLALCHEMY_ECHO = True



class TestingConfig(Config):
    """
    Testing Configurations
       """
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/amazon_test_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    """
    Production Configurations
       """
    DEBUG = False


app_config = {

    'development': DevelopementConfig,
    'Testing': TestingConfig,
    'production': ProductionConfig
}

