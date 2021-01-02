import os
from flask_ecommerce_class import create_app ,db

config_name = os.getenv('FLASK_CONFIG','development')
# by default is development, if flask_config is not set
app = create_app(config_name)

if __name__=='__main__':
    with app.app_context():  # Allow application context
        db.create_all()  # create tables only
    app.run()




