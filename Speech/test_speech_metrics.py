from Speech.speech_metrics import SpeechMetrics

metrics = SpeechMetrics()

transcript = """

Hello.

My name is Krishna.

I am pursuing B.Tech in Artificial Intelligence
and Data Science.

I enjoy Machine Learning and Python.

"""

duration = 24

report = metrics.analyze(

    transcript,

    duration

)

for key, value in report.items():

    print(

        f"{key} : {value}"

    )