import cv2

from Emotion_analysis.camera import Camera
from Emotion_analysis.face_detector import FaceDetector
from Emotion_analysis.emotion_detector import EmotionDetector
from Emotion_analysis.emotion_smoother import EmotionSmoother


camera = Camera()

face_detector = FaceDetector()

emotion_detector = EmotionDetector()

smoother = EmotionSmoother()

while True:

    frame = camera.get_frame()

    if frame is None:
        break

    faces = face_detector.detect(frame)

    frame = face_detector.draw_faces(frame, faces)

    emotion, confidence = emotion_detector.analyze(frame)

    smoother.update(emotion)

    stable_emotion = smoother.get_emotion()

    cv2.putText(

        frame,

        f"Emotion : {stable_emotion}",

        (20,40),

        cv2.FONT_HERSHEY_SIMPLEX,

        0.8,

        (0,255,0),

        2

    )

    cv2.putText(

        frame,

        f"Confidence : {confidence:.1f}%",

        (20,75),

        cv2.FONT_HERSHEY_SIMPLEX,

        0.8,

        (255,0,0),

        2

    )

    cv2.imshow(

        "Emotion Detection",

        frame

    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()