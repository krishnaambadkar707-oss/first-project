from Speech.voice_interview import VoiceInterview

bot = VoiceInterview()

question = "What is Machine Learning?"

ideal = """
Machine Learning is a subset of Artificial Intelligence
that enables computers to learn patterns
from data without explicit programming.
"""

report = bot.conduct_interview(

    question,

    ideal

)

print()

print("=" * 60)

print("INTERVIEW REPORT")

print("=" * 60)

for key, value in report.items():

    print()

    print(key)

    print(value)