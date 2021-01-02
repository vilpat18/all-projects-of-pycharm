import os
from flask_practice import create_app , db

config_name = os.getenv('flask_practice','Development')
app = create_app(config_name)

if __name__=='__main__':
    with app.app_context(): #allow aplication context
        db.create_all()
        app.run(debug=True,port=5999)


