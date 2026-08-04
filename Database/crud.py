from sqlalchemy.orm import Session

from Database.models import User


def create_user(db: Session, full_name, email, password):

    user = User(
        full_name=full_name,
        email=email,
        password=password
    )

    db.add(user)

    db.commit()

    db.refresh(user)

    return user


def get_user_by_email(db: Session, email):

    return db.query(User).filter(User.email == email).first()


def get_all_users(db: Session):

    return db.query(User).all()