# config.py
class Config():
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'  # or use PostgreSQL/MySQL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
