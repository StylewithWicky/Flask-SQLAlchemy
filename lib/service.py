from lib.models import db,User

def create_user(id,username,email):
    create_user=User(id='1' ,username='alice',email='alice@example.com')
    db.session.add(create_user)
    db.session.commit()
    return create_user

def get_all_users():
    return User.query.all()