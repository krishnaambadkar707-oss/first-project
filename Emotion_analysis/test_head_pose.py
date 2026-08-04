import cv2

from Emotion_analysis.camera import Camera
from Emotion_analysis.head_pose import HeadPoseEstimator

camera = Camera()

estimator = HeadPoseEstimator()

while True:

    frame = camera.get_frame()

    if frame is None:
        break

    frame, direction, pitch, yaw, roll = estimator.estimate(frame)

    cv2.putText(
        frame,
        direction,
        (20,40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0,255,0),
        2
    )

    cv2.putText(
        frame,
        f"Pitch : {pitch:.1f}",
        (20,80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255,255,0),
        2
    )

    cv2.putText(
        frame,
        f"Yaw : {yaw:.1f}",
        (20,120),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255,255,0),
        2
    )

    cv2.putText(
        frame,
        f"Roll : {roll:.1f}",
        (20,160),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255,255,0),
        2
    )

    cv2.imshow("Head Pose Estimation", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()