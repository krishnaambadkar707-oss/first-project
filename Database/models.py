from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import DateTime
from sqlalchemy import Text
from sqlalchemy.sql import func

from Database.database import Base


# -------------------------
# User Table
# -------------------------

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    full_name = Column(String(100))

    email = Column(String(120), unique=True)

    password = Column(String(200))

    created_at = Column(DateTime(timezone=True), server_default=func.now())


# -------------------------
# Resume Table
# -------------------------

class Resume(Base):

    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer)

    resume_name = Column(String(200))

    skills = Column(Text)

    education = Column(Text)

    projects = Column(Text)

    uploaded_at = Column(DateTime(timezone=True), server_default=func.now())


# -------------------------
# Interview Table
# -------------------------

class Interview(Base):

    __tablename__ = "interviews"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer)

    domain = Column(String(100))

    difficulty = Column(String(30))

    interview_type = Column(String(50))

    total_score = Column(Float)

    technical_score = Column(Float)

    communication_score = Column(Float)

    confidence_score = Column(Float)

    created_at = Column(DateTime(timezone=True), server_default=func.now())


# -------------------------
# Question Table
# -------------------------

class Question(Base):

    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)

    domain = Column(String(100))

    difficulty = Column(String(30))

    question = Column(Text)

    answer = Column(Text)


# -------------------------
# Answer Table
# -------------------------

class Answer(Base):

    __tablename__ = "answers"

    id = Column(Integer, primary_key=True)

    interview_id = Column(Integer)

    question_id = Column(Integer)

    user_answer = Column(Text)

    obtained_marks = Column(Float)

    feedback = Column(Text)


# -------------------------
# Emotion Table
# -------------------------

class Emotion(Base):

    __tablename__ = "emotion_analysis"

    id = Column(Integer, primary_key=True)

    interview_id = Column(Integer)

    dominant_emotion = Column(String(50))

    happy = Column(Float)

    neutral = Column(Float)

    sad = Column(Float)

    angry = Column(Float)

    surprise = Column(Float)

    fear = Column(Float)

    confidence = Column(Float)


# -------------------------
# Report Table
# -------------------------

class Report(Base):

    __tablename__ = "reports"

    id = Column(Integer, primary_key=True)

    interview_id = Column(Integer)

    pdf_path = Column(String(300))

    created_at = Column(DateTime(timezone=True), server_default=func.now())