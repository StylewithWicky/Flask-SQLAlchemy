from flask import Flask
from config import Config
from lib.models import db  # Do not create a new db here!

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app



