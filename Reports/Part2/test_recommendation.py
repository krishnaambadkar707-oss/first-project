from Part2.recommendation_engine import RecommendationEngine

engine = RecommendationEngine()

report = engine.generate(

    technical=92,

    communication=84,

    behavior=88,

    resume=76

)

print("=" * 60)

print("Overall :", report["Overall"])

print()

print("Hiring Recommendation :")

print(report["Hiring"])

print()

print("Strengths")

for item in report["Strengths"]:

    print("✔", item)

print()

print("Areas to Improve")

for item in report["Improvements"]:

    print("-", item)

print()

print("Suggestions")

for item in report["Recommendations"]:

    print("•", item)