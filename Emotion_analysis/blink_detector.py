import cv2
import mediapipe as mp
import math
import time


class BlinkDetector:

    def __init__(self):

        self.face_mesh = mp.solutions.face_mesh.FaceMesh(
            max_num_faces=1,
            refine_landmarks=True
        )

        # Left Eye
        self.LEFT = [33, 160, 158, 133, 153, 144]

        # Right Eye
        self.RIGHT = [362, 385, 387, 263, 373, 380]

        self.blinks = 0
        self.closed = False

        self.start_time = time.time()

    def distance(self, p1, p2):

        return math.hypot(
            p1[0]-p2[0],
            p1[1]-p2[1]
        )

    def ear(self, eye):

        A = self.distance(eye[1], eye[5])

        B = self.distance(eye[2], eye[4])

        C = self.distance(eye[0], eye[3])

        return (A + B) / (2.0 * C)

    def detect(self, frame):

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        result = self.face_mesh.process(rgb)

        if not result.multi_face_landmarks:

            return frame, "No Face", self.blinks, 0

        h, w, _ = frame.shape

        face = result.multi_face_landmarks[0]

        landmarks = []

        for lm in face.landmark:

            landmarks.append(
                (int(lm.x*w), int(lm.y*h))
            )

        left_eye = [landmarks[i] for i in self.LEFT]

        right_eye = [landmarks[i] for i in self.RIGHT]

        leftEAR = self.ear(left_eye)

        rightEAR = self.ear(right_eye)

        ear = (leftEAR + rightEAR) / 2

        if ear < 0.22:

            if not self.closed:

                self.blinks += 1

                self.closed = True

        else:

            self.closed = False

        elapsed = time.time() - self.start_time

        bpm = 0

        if elapsed > 0:

            bpm = (self.blinks / elapsed) * 60

        status = "Open"

        if ear < 0.22:
            status = "Closed"

        return frame, status, self.blinks, bpm