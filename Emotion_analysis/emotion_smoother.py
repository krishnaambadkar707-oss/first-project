from collections import Counter


class EmotionSmoother:

    def __init__(self, history_size=10):

        self.history = []

        self.history_size = history_size

    def update(self, emotion):

        self.history.append(emotion)

        if len(self.history) > self.history_size:
            self.history.pop(0)

    def get_emotion(self):

        if not self.history:
            return "Unknown"

        counter = Counter(self.history)

        return counter.most_common(1)[0][0]