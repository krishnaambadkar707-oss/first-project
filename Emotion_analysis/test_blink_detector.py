import cv2

from Emotion_analysis.camera import Camera
from Emotion_analysis.blink_detector import BlinkDetector

camera = Camera()

detector = BlinkDetector()

while True:

    frame = camera.get_frame()

    if frame is None:
        break

    frame, status, blinks, bpm = detector.detect(frame)

    cv2.putText(
        frame,
        f"Eye : {status}",
        (20,40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0,255,0),
        2
    )

    cv2.putText(
        frame,
        f"Blinks : {blinks}",
        (20,80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255,0,0),
        2
    )

    cv2.putText(
        frame,
        f"Blink Rate : {bpm:.1f}/min",
        (20,120),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0,255,255),
        2
    )

    cv2.imshow(
        "Blink Detection",
        frame
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()