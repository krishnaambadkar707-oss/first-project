import sqlite3
import os


class Database:

    def __init__(self):

        os.makedirs("data", exist_ok=True)

        self.connection = sqlite3.connect(
            "data/interview.db",
            check_same_thread=False
        )

        self.cursor = self.connection.cursor()

        self.create_table()

    def create_table(self):

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS interviews(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            candidate_name TEXT,

            email TEXT,

            job_role TEXT,

            interview_date TEXT,

            technical REAL,

            communication REAL,

            behavior REAL,

            resume REAL,

            overall REAL,

            response_time REAL,

            wpm REAL,

            fluency REAL,

            recommendation TEXT,

            hiring TEXT

        )

        """)

        self.connection.commit()