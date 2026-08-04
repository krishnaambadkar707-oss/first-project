from Part1.score_calculator import ScoreCalculator

calculator = ScoreCalculator()

technical = calculator.technical_score(

    semantic=95,

    keywords=90,

    grammar=100,

    completeness=88

)

communication = calculator.communication_score(

    wpm_score=90,

    fluency=92,

    response_time=88,

    clarity=95

)

behavior = calculator.behavior_score(

    eye_contact=94,

    head_pose=90,

    emotion=91,

    smile=80,

    blink=87,

    face_visibility=100

)

overall = calculator.overall_score(

    technical,

    communication,

    behavior,

    resume=92

)

print("=" * 40)

print("Technical :", technical)

print("Communication :", communication)

print("Behavior :", behavior)

print("Overall :", overall)

print("Grade :", calculator.grade(overall))