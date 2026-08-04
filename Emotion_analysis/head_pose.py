import cv2
import mediapipe as mp
import numpy as np


class HeadPoseEstimator:

    def __init__(self):

        self.face_mesh = mp.solutions.face_mesh.FaceMesh(
            max_num_faces=1,
            refine_landmarks=True
        )

    def estimate(self, frame):

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        result = self.face_mesh.process(rgb)

        if not result.multi_face_landmarks:

            return frame, "No Face", 0, 0, 0

        h, w, _ = frame.shape

        face = result.multi_face_landmarks[0]

        face_2d = []
        face_3d = []

        landmark_ids = [
            33,   # Left Eye
            263,  # Right Eye
            1,    # Nose
            61,   # Left Mouth
            291,  # Right Mouth
            199   # Chin
        ]

        for idx in landmark_ids:

            lm = face.landmark[idx]

            x = int(lm.x * w)
            y = int(lm.y * h)

            face_2d.append([x, y])

            face_3d.append([x, y, lm.z])

        face_2d = np.array(face_2d, dtype=np.float64)
        face_3d = np.array(face_3d, dtype=np.float64)

        focal_length = w

        cam_matrix = np.array([
            [focal_length, 0, w / 2],
            [0, focal_length, h / 2],
            [0, 0, 1]
        ])

        dist = np.zeros((4, 1))

        success, rot_vec, trans_vec = cv2.solvePnP(
            face_3d,
            face_2d,
            cam_matrix,
            dist
        )

        if not success:

            return frame, "Unknown", 0, 0, 0

        rmat, _ = cv2.Rodrigues(rot_vec)

        angles, _, _, _, _, _ = cv2.RQDecomp3x3(rmat)

        pitch = angles[0] * 360
        yaw = angles[1] * 360
        roll = angles[2] * 360

        if yaw < -12:
            direction = "Looking Left"

        elif yaw > 12:
            direction = "Looking Right"

        elif pitch < -10:
            direction = "Looking Down"

        elif pitch > 10:
            direction = "Looking Up"

        else:
            direction = "Looking Straight"

        return frame, direction, pitch, yaw, roll