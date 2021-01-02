from flask_ecommerce import create_app, db
import os

config_name = os.getenv("FLASK_CONFIG",'development')
app = create_app(config_name)

if __name__=="__main__":
     app.run(debug=True,port=5010)
     with app.app_context():
         db.create_all()



