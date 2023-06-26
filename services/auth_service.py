from models import db, User


def create_user(username, password, name=None):
    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
