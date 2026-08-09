from sqlalchemy.orm import Session

from Database.models import User
from Database.models import Resume
from Database.models import Interview
from Database.models import Answer


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


def get_user_by_id(db: Session, user_id):

    return db.query(User).filter(User.id == user_id).first()


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


def create_interview(

    db: Session,

    user_id,

    domain,

    difficulty,

    interview_type,

    total_score,

    technical_score,

    communication_score,

    confidence_score,

):

    interview = Interview(

        user_id=user_id,

        domain=domain,

        difficulty=difficulty,

        interview_type=interview_type,

        total_score=total_score,

        technical_score=technical_score,

        communication_score=communication_score,

        confidence_score=confidence_score,

    )

    db.add(interview)

    db.commit()

    db.refresh(interview)

    return interview


def create_answer(

    db: Session,

    interview_id,

    question_id,

    user_answer,

    obtained_marks,

    feedback,

):

    answer = Answer(

        interview_id=interview_id,

        question_id=question_id,

        user_answer=user_answer,

        obtained_marks=obtained_marks,

        feedback=feedback,

    )

    db.add(answer)

    db.commit()

    db.refresh(answer)

    return answer


def get_interviews_by_user(db: Session, user_id):

    return (
        db.query(Interview)
        .filter(Interview.user_id == user_id)
        .order_by(Interview.created_at.desc())
        .all()
    )


def get_interview_by_id(db: Session, interview_id):

    return db.query(Interview).filter(Interview.id == interview_id).first()


def get_answers_by_interview(db: Session, interview_id):

    return (
        db.query(Answer)
        .filter(Answer.interview_id == interview_id)
        .all()
    )