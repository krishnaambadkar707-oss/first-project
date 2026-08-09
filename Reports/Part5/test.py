from Reports.Part5.pdf_report import PDFReport

generator = PDFReport()

report = {

    "name":"Krishna Ambadkar",

    "email":"krishna@gmail.com",

    "role":"AI Engineer",

    "date":"17 July 2026",

    "technical":92,

    "communication":88,

    "behavior":90,

    "resume":91,

    "overall":91,

    "response_time":"2.4 sec",

    "speech":{

        "Words":132,

        "WPM":118,

        "Fluency":96

    },

    "recommendations":[

        "Improve SQL concepts",

        "Maintain eye contact",

        "Excellent Python knowledge"

    ],

    "hiring":"Highly Recommended"

}

pdf = generator.generate(report)

print(pdf)