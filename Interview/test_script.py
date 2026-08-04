import cv2

from Interview.confidence import ConfidenceAnalyzer

cap = cv2.VideoCapture(0)

analyzer = ConfidenceAnalyzer()

while True:

    ret, frame = cap.read()

    if not ret:
        break

    report = analyzer.analyze(frame)

    if report:

        cv2.putText(

            frame,

            f"Confidence: {report['Confidence']}",

            (20,40),

            cv2.FONT_HERSHEY_SIMPLEX,

            1,

            (0,255,0),

            2

        )

    cv2.imshow(

        "Interview",

        frame

    )

    if cv2.waitKey(1) == 27:

        break

cap.release()

cv2.destroyAllWindows()