# seed.py
from lib.models import User, db
from app import create_app

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    users = [
        User(username="alice", email="alice@example.com"),
        User(username="bob", email="bob@example.com"),
        User(username="charlie", email="charlie@example.com"),
        User(username="dave", email="dave@example.com"),
    ]

    db.session.add_all(users)
    db.session.commit()

    print("Seeded with data.")
