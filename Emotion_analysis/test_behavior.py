from Emotion_analysis.confidence_estimator import ConfidenceEstimator
from Emotion_analysis.behavior_analyzer import BehaviorAnalyzer

confidence = ConfidenceEstimator()

score = confidence.calculate(

    eye_contact=90,

    emotion_score=88,

    head_pose_score=92,

    smile_score=75,

    blink_score=82,

    face_visibility=100,

    response_time=85

)

behavior = BehaviorAnalyzer()

report = behavior.analyze(

    confidence=score,

    eye_contact=90,

    emotion="Happy",

    smile="Slight Smile",

    blink_rate=18

)

print(report)