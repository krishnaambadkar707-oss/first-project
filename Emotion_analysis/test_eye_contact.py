import cv2

from Emotion_analysis.camera import Camera
from Emotion_analysis.eye_contact import EyeContactDetector

camera = Camera()

detector = EyeContactDetector()

while True:

    frame = camera.get_frame()

    if frame is None:
        break

    frame, score, status = detector.analyze(frame)

    cv2.putText(
        frame,
        f"Eye Contact : {score}%",
        (20,40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0,255,0),
        2
    )

    cv2.putText(
        frame,
        status,
        (20,80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255,0,0),
        2
    )

    cv2.imshow(
        "Eye Contact Detection",
        frame
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()