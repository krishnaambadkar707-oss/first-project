import os
import numpy as np
import matplotlib.pyplot as plt


class ChartGenerator:

    def __init__(self):

        self.output_dir = "assets/charts"

        os.makedirs(self.output_dir, exist_ok=True)

    # ----------------------------
    # Save Chart
    # ----------------------------
    def save(self, name):

        path = os.path.join(

            self.output_dir,

            name

        )

        plt.tight_layout()

        plt.savefig(path, dpi=300)

        plt.close()

        return path
    
    def radar_chart(

        self,

        technical,

        communication,

        behavior,

        resume

    ):

        labels = [

            "Technical",

            "Communication",

            "Behavior",

            "Resume"

        ]

        values = [

            technical,

            communication,

            behavior,

            resume

        ]

        values += values[:1]

        angles = np.linspace(

            0,

            2*np.pi,

            len(labels),

            endpoint=False

        ).tolist()

        angles += angles[:1]

        plt.figure(figsize=(6,6))

        ax = plt.subplot(111, polar=True)

        ax.plot(

            angles,

            values,

            linewidth=2

        )

        ax.fill(

            angles,

            values,

            alpha=0.25

        )

        ax.set_xticks(

            angles[:-1]

        )

        ax.set_xticklabels(

            labels

        )

        ax.set_ylim(

            0,

            100

        )

        return self.save(

            "radar.png"

        )
    
    def bar_chart(

        self,

        technical,

        communication,

        behavior,

        resume

    ):

        labels = [

            "Technical",

            "Communication",

            "Behavior",

            "Resume"

        ]

        values = [

            technical,

            communication,

            behavior,

            resume

        ]

        plt.figure(figsize=(8,5))

        plt.bar(

            labels,

            values

        )

        plt.ylim(

            0,

            100

        )

        plt.ylabel("Score")

        plt.title("Interview Performance")

        return self.save(

            "bar.png"

        )
    
    def pie_chart(

        self,

        technical,

        communication,

        behavior,

        resume

    ):

        labels = [

            "Technical",

            "Communication",

            "Behavior",

            "Resume"

        ]

        values = [

            technical,

            communication,

            behavior,

            resume

        ]

        plt.figure(figsize=(6,6))

        plt.pie(

            values,

            labels=labels,

            autopct="%1.1f%%"

        )

        plt.title(

            "Interview Score Distribution"

        )

        return self.save(

            "pie.png"

        )    
    
    def question_chart(

        self,

        scores

    ):

        questions = [

            f"Q{i+1}"

            for i in range(

                len(scores)

            )

        ]

        plt.figure(figsize=(8,5))

        plt.plot(

            questions,

            scores,

            marker="o"

        )

        plt.ylim(

            0,

            100

        )

        plt.title(

            "Question-wise Performance"

        )

        plt.ylabel(

            "Score"

        )

        return self.save(

            "question.png"

        )

def performance_trend(

    self,

    scores

):

    interviews = [

        f"I{i+1}"

        for i in range(

            len(scores)

        )

    ]

    plt.figure(

        figsize=(8,5)

    )

    plt.plot(

        interviews,

        scores,

        marker="o",

        linewidth=3

    )

    plt.ylim(

        0,

        100

    )

    plt.title(

        "Interview Performance"

    )

    plt.ylabel(

        "Overall Score"

    )

    return self.save(

        "performance.png"

    )        