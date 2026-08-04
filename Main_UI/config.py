import os

# Project Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
RESUME_FOLDER = os.path.join(UPLOAD_FOLDER, "resumes")
REPORT_FOLDER = os.path.join(UPLOAD_FOLDER, "reports")
RECORDING_FOLDER = os.path.join(UPLOAD_FOLDER, "recordings")

DATABASE_NAME = "interview_bot.db"
CHART_FOLDER = "assets/charts"

APP_NAME = "AI Powered Interview Bot"
MODEL = "all-MiniLM-L6-v2"
VERSION = "1.0"

WHISPER_MODEL = "base"
INTERVIEW_TIME = 30

DEBUG = True