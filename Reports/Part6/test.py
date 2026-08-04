from Part6.interview_history import InterviewHistory

history = InterviewHistory()

sample = {

    "name":"Krishna Ambadkar",

    "email":"krishna@gmail.com",

    "role":"AI Engineer",

    "date":"17 July 2026",

    "technical":93,

    "communication":89,

    "behavior":91,

    "resume":92,

    "overall":91,

    "response_time":2.4,

    "speech":{

        "WPM":118,

        "Fluency":95

    },

    "recommendations":[

        "Improve SQL",

        "Practice DSA"

    ],

    "hiring":"Highly Recommended"

}

history.save(sample)

print("Interview Saved Successfully")