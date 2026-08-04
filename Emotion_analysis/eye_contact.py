import cv2
import mediapipe as mp
import math


class EyeContactDetector:

    def __init__(self):

        self.face_mesh = mp.solutions.face_mesh.FaceMesh(
            static_image_mode=False,
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )

        # MediaPipe landmark indices
        self.LEFT_IRIS = [474, 475, 476, 477]
        self.RIGHT_IRIS = [469, 470, 471, 472]

        self.LEFT_EYE = [33, 133]
        self.RIGHT_EYE = [362, 263]

    def _distance(self, p1, p2):
        return math.hypot(
            p1[0] - p2[0],
            p1[1] - p2[1]
        )

    def analyze(self, frame):

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        result = self.face_mesh.process(rgb)

        if not result.multi_face_landmarks:
            return frame, 0, "No Face"

        h, w, _ = frame.shape

        face = result.multi_face_landmarks[0]

        landmarks = []

        for lm in face.landmark:
            landmarks.append(
                (int(lm.x * w), int(lm.y * h))
            )

        # Draw iris
        for idx in self.LEFT_IRIS + self.RIGHT_IRIS:
            cv2.circle(
                frame,
                landmarks[idx],
                2,
                (0, 255, 0),
                -1
            )

        left_corner = landmarks[self.LEFT_EYE[0]]
        right_corner = landmarks[self.LEFT_EYE[1]]

        iris = landmarks[474]

        eye_width = self._distance(
            left_corner,
            right_corner
        )

        iris_offset = self._distance(
            left_corner,
            iris
        )

        ratio = iris_offset / eye_width

        if 0.35 <= ratio <= 0.65:

            attention = 100

            status = "Looking"

        else:

            attention = 40

            status = "Looking Away"

        return frame, attention, status