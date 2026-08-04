import cv2

from Emotion_analysis.camera import Camera
from Emotion_analysis.smile_detector import SmileDetector

camera = Camera()

detector = SmileDetector()

while True:

    frame = camera.get_frame()

    if frame is None:
        break

    frame, status, score = detector.detect(frame)

    cv2.putText(
        frame,
        f"Smile : {status}",
        (20,40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0,255,0),
        2
    )

    cv2.putText(
        frame,
        f"Smile Score : {score:.1f}%",
        (20,80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255,0,0),
        2
    )

    cv2.imshow(
        "Smile Detection",
        frame
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()