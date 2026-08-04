import time


class ResponseTimer:

    def __init__(self):

        self.start_time = None
        self.end_time = None

    def start(self):

        self.start_time = time.perf_counter()

    def stop(self):

        self.end_time = time.perf_counter()

    def response_time(self):

        if self.start_time is None or self.end_time is None:
            return 0

        return round(
            self.end_time - self.start_time,
            2
        )

    def response_score(self):

        t = self.response_time()

        if t <= 2:
            return 100

        elif t <= 4:
            return 90

        elif t <= 6:
            return 75

        elif t <= 10:
            return 60

        else:
            return 40

    def feedback(self):

        t = self.response_time()

        if t <= 2:

            return "Excellent response time."

        elif t <= 4:

            return "Quick and natural response."

        elif t <= 6:

            return "Reasonable thinking time."

        elif t <= 10:

            return "Long pause before answering."

        return "Very long delay before speaking."