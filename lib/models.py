from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)




    
    
    def __repr__(self):
        return f"< User : {self.username} >"