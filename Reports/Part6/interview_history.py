from Reports.Part6.database import Database


class InterviewHistory:

    def __init__(self):

        self.db = Database()

    # -----------------------------
    # Save Interview
    # -----------------------------
    def save(self, report):

        query = """

        INSERT INTO interviews(

        candidate_name,

        email,

        job_role,

        interview_date,

        technical,

        communication,

        behavior,

        resume,

        overall,

        response_time,

        wpm,

        fluency,

        recommendation,

        hiring

        )

        VALUES(

        ?,?,?,?,?,?,?,?,?,?,?,?,?,?

        )

        """

        values = (

            report["name"],

            report["email"],

            report["role"],

            report["date"],

            report["technical"],

            report["communication"],

            report["behavior"],

            report["resume"],

            report["overall"],

            report["response_time"],

            report["speech"]["WPM"],

            report["speech"]["Fluency"],

            ", ".join(report["recommendations"]),

            report["hiring"]

        )

        self.db.cursor.execute(query, values)

        self.db.connection.commit()

    def get_all(self):

        self.db.cursor.execute("""

        SELECT *

        FROM interviews

        ORDER BY id DESC

        """)

        return self.db.cursor.fetchall()        
    
    def search(self, name):

        self.db.cursor.execute("""

        SELECT *

        FROM interviews

        WHERE candidate_name LIKE ?

        ORDER BY interview_date DESC

        """,

        ("%"+name+"%",)

        )

        return self.db.cursor.fetchall()    
    
    def delete(self, interview_id):

        self.db.cursor.execute("""

        DELETE FROM interviews

        WHERE id=?

        """,

        (interview_id,)

        )

        self.db.connection.commit()