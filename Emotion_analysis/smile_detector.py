import cv2
import mediapipe as mp
import math


class SmileDetector:

    def __init__(self):

        self.face_mesh = mp.solutions.face_mesh.FaceMesh(
            max_num_faces=1,
            refine_landmarks=True
        )

        # Mouth landmarks
        self.LEFT_MOUTH = 61
        self.RIGHT_MOUTH = 291
        self.UPPER_LIP = 13
        self.LOWER_LIP = 14

    def distance(self, p1, p2):

        return math.hypot(
            p1[0] - p2[0],
            p1[1] - p2[1]
        )

    def detect(self, frame):

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        result = self.face_mesh.process(rgb)

        if not result.multi_face_landmarks:

            return frame, "No Face", 0

        h, w, _ = frame.shape

        face = result.multi_face_landmarks[0]

        landmarks = []

        for lm in face.landmark:

            landmarks.append(
                (int(lm.x * w), int(lm.y * h))
            )

        left = landmarks[self.LEFT_MOUTH]
        right = landmarks[self.RIGHT_MOUTH]

        upper = landmarks[self.UPPER_LIP]
        lower = landmarks[self.LOWER_LIP]

        mouth_width = self.distance(left, right)
        mouth_height = self.distance(upper, lower)

        ratio = mouth_width / (mouth_height + 1)

        # Convert ratio to percentage
        smile_percentage = min(max((ratio - 6) * 25, 0), 100)

        if smile_percentage > 60:
            status = "Smiling"
        elif smile_percentage > 30:
            status = "Slight Smile"
        else:
            status = "Neutral"

        # Draw mouth landmarks
        for point in [left, right, upper, lower]:
            cv2.circle(frame, point, 3, (0, 255, 0), -1)

        return frame, status, smile_percentage