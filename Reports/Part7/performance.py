from Part6.interview_history import InterviewHistory
import matplotlib.pyplot as plt


class PerformanceAnalyzer:

    def __init__(self):

        self.history = InterviewHistory()

    def load_candidate(self, candidate):

        interviews = self.history.search(candidate)

        interviews.reverse()

        return interviews
    
    def overall_scores(self, interviews):

        return [

            row[9]

            for row in interviews

        ]

    def technical_scores(self, interviews):

        return [

            row[5]

            for row in interviews

        ]

    def communication_scores(

        self,

        interviews

    ):

        return [

            row[6]

            for row in interviews

        ]

    def behavior_scores(

        self,

        interviews

    ):

        return [

            row[7]

            for row in interviews

        ]

    def improvement(

        self,

        interviews

    ):

        if len(interviews) < 2:

            return 0

        first = interviews[0][9]

        last = interviews[-1][9]

        improvement = (

            (last-first)

            / first

        ) * 100

        return round(

            improvement,

            2

        )                       