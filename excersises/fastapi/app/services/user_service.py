from app.models.user_model import UserModel

def create_user(db, user):
    db_user = UserModel(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db):
    return db.query(UserModel).all()
