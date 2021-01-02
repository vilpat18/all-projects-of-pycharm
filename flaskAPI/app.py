import app as app

from flaskAPI import create_app, db
import os
app.config['SECRET_KEY']='Th1s1ss3cr3t'
config_name = os.getenv("FLASK_CONFIG",'development')
app = create_app(config_name)

if __name__=="__main__":
     app.run(debug=True,port=5050)
     with app.app_context():
         db.create_all()