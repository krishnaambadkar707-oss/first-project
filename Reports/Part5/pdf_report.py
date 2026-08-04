from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image
)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import inch
import os


class PDFReport:

    def __init__(self):

        self.styles = getSampleStyleSheet()

        os.makedirs("reports/output", exist_ok=True)

    def generate(self, report):

        filename = "reports/output/interview_report.pdf"

        pdf = SimpleDocTemplate(filename)

        elements = []

        title = Paragraph(
            "<b><font size=20>AI Interview Report</font></b>",
            self.styles["Title"]
        )

        elements.append(title)

        elements.append(Spacer(1, 0.3 * inch))

        elements.append(

            Paragraph(

                "<b>Candidate Details</b>",

                self.styles["Heading2"]

            )

        )

        data = [

            ["Name", report["name"]],

            ["Email", report["email"]],

            ["Role", report["role"]],

            ["Interview Date", report["date"]]

        ]

        table = Table(data)

        table.setStyle(

            TableStyle([

                ("BACKGROUND",(0,0),(-1,0),colors.lightgrey),

                ("GRID",(0,0),(-1,-1),1,colors.black),

                ("BOTTOMPADDING",(0,0),(-1,0),8)

            ])

        )

        elements.append(table)

        elements.append(Spacer(1,0.3*inch))

        elements.append(

            Paragraph(

                "<b>Interview Scores</b>",

                self.styles["Heading2"]

            )

        )

        score_table = Table([

            ["Category","Score"],

            ["Technical",report["technical"]],

            ["Communication",report["communication"]],

            ["Behavior",report["behavior"]],

            ["Resume",report["resume"]],

            ["Overall",report["overall"]]

        ])

        score_table.setStyle(

            TableStyle([

                ("BACKGROUND",(0,0),(-1,0),colors.lightblue),

                ("GRID",(0,0),(-1,-1),1,colors.black)

            ])

        )

        elements.append(score_table)

        elements.append(Spacer(1,0.3*inch))

        elements.append(

            Paragraph(

                "<b>Speech Analysis</b>",

                self.styles["Heading2"]

            )

        )

        speech = report["speech"]

        speech_table = Table([

            ["Words", speech["Words"]],

            ["WPM", speech["WPM"]],

            ["Fluency", speech["Fluency"]],

            ["Response Time", report["response_time"]]

        ])

        speech_table.setStyle(

            TableStyle([

                ("GRID",(0,0),(-1,-1),1,colors.black)

            ])

        )

        elements.append(speech_table)

        elements.append(

            Spacer(1,0.3*inch)

        )

        elements.append(

            Paragraph(

                "<b>AI Recommendations</b>",

                self.styles["Heading2"]

            )

        )

        for item in report["recommendations"]:

            elements.append(

                Paragraph(

                    "• "+item,

                    self.styles["BodyText"]

                )

            )

        charts = [

            "assets/charts/radar.png",

            "assets/charts/bar.png",

            "assets/charts/pie.png"

        ]

        for chart in charts:

            if os.path.exists(chart):

                elements.append(

                    Spacer(1,0.2*inch)

                )

                elements.append(

                    Image(

                        chart,

                        width=5*inch,

                        height=4*inch

                    )

                )    

        elements.append(

            Spacer(1,0.3*inch)

        )

        elements.append(

            Paragraph(

                "<b>Final Recommendation</b>",

                self.styles["Heading2"]

            )

        )

        elements.append(

            Paragraph(

                report["hiring"],

                self.styles["BodyText"]

            )

        )

        pdf.build(elements)

        return filename