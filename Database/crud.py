from sqlalchemy.orm import Session

from Database.models import User
from Database.models import Resume


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


def create_resume(db: Session, user_id, resume_name, skills, education, projects):

    resume = Resume(
        user_id=user_id,
        resume_name=resume_name,
        skills=skills,
        education=education,
        projects=projects,
    )

    db.add(resume)

    db.commit()

    db.refresh(resume)

    return resume


def get_resumes_by_user(db: Session, user_id):

    return (
        db.query(Resume)
        .filter(Resume.user_id == user_id)
        .order_by(Resume.uploaded_at.desc())
        .all()
    )