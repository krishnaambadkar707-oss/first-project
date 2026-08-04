import cv2
import mediapipe as mp
import numpy as np


class ConfidenceAnalyzer:

    def __init__(self):

        self.mp_face = mp.solutions.face_mesh

        self.face_mesh = self.mp_face.FaceMesh(

            static_image_mode=False,

            max_num_faces=1,

            refine_landmarks=True,

            min_detection_confidence=0.5,

            min_tracking_confidence=0.5

        )

        self.LEFT_EYE = [33, 160, 158, 133, 153, 144]
        self.RIGHT_EYE = [362, 385, 387, 263, 373, 380]

    # -------------------------
    # Eye Aspect Ratio
    # -------------------------

    def eye_ratio(self, points):

        vertical = np.linalg.norm(points[1] - points[5]) + \
                   np.linalg.norm(points[2] - points[4])

        horizontal = np.linalg.norm(points[0] - points[3])

        return vertical / (2 * horizontal)

    # -------------------------
    # Analyze One Frame
    # -------------------------

    def analyze(self, frame):

        rgb = cv2.cvtColor(

            frame,

            cv2.COLOR_BGR2RGB

        )

        results = self.face_mesh.process(rgb)

        if not results.multi_face_landmarks:

            return None

        landmarks = results.multi_face_landmarks[0]

        h, w, _ = frame.shape

        pts = []

        for lm in landmarks.landmark:

            pts.append(

                np.array([

                    lm.x * w,

                    lm.y * h

                ])

            )

        left = np.array(

            [pts[i] for i in self.LEFT_EYE]

        )

        right = np.array(

            [pts[i] for i in self.RIGHT_EYE]

        )

        left_ratio = self.eye_ratio(left)

        right_ratio = self.eye_ratio(right)

        blink = (

            left_ratio < 0.20

            or

            right_ratio < 0.20

        )

        eye_contact = round(

            min(

                100,

                ((left_ratio + right_ratio) / 0.60) * 100

            ),

            2

        )

        confidence = round(

            eye_contact * 0.8 +

            (0 if blink else 20),

            2

        )

        return {

            "Eye Contact": eye_contact,

            "Blink": blink,

            "Confidence": confidence

        }