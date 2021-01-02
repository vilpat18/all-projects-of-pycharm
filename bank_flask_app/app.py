from bank_flask_app import create_app,db
import os

config_name = os.getenv('FLASK_CONFIG','development')
app = create_app(config_name)

if __name__=='__main__':
    with app.app_context():#allow application context
        db.create_all() #create table only
    app.run(debug=True,port=5998)

