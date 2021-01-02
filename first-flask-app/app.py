from flask_registration import create_app, db
import os

config_name = os.getenv("FLASK_CONFIG",'developement')
app =create_app(config_name)

if __name__=='__main__':
    app.run(debug=True,port=5000)
    with app.app_context():
     db.create_all()



