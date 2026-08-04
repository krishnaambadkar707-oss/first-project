import cv2

from Emotion_analysis.camera import Camera
from Emotion_analysis.face_detector import FaceDetector


camera = Camera()

detector = FaceDetector()

while True:

    frame = camera.get_frame()

    if frame is None:
        break

    faces = detector.detect(frame)

    frame = detector.draw_faces(
        frame,
        faces
    )

    cv2.putText(

        frame,

        f"Faces Detected : {len(faces)}",

        (20, 40),

        cv2.FONT_HERSHEY_SIMPLEX,

        0.8,

        (0, 255, 0),

        2

    )

    cv2.imshow(

        "AI Interview Bot",

        frame

    )

    key = cv2.waitKey(1)

    if key == ord("q"):

        break


camera.release()