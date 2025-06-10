from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from lib.models import db, User

app = Flask(__name__)
app.config.from_object(Config)

#db.init_app(app)
db =SQLAlchemy(app)

def create_app():
        app=Flask(__name__)
        app.config.from_object(Config)

        db.init_app(app)

        with app.app_context():
                from lib.models import User
                db.create_all()
        return app



#@app.route('/')
#def index():
    #return "<h1>Hello, Flask-SQLAlchemy!</h1>"

#if __name__ == '__main__':
    #with app.app_context():
        #db.create_all()  # creates tables
        #app.run(port=5555, debug=True)