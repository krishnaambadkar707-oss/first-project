import streamlit as st

from Part7.performance import PerformanceAnalyzer
from Part3.charts import ChartGenerator


def show_comparison():

    st.title(

        "Performance Comparison"

    )

    candidate = st.text_input(

        "Candidate Name"

    )

    if candidate:

        analyzer = PerformanceAnalyzer()

        interviews = analyzer.load_candidate(

            candidate

        )

        if len(interviews) == 0:

            st.warning(

                "Candidate not found."

            )

            return

        scores = analyzer.overall_scores(

            interviews

        )

        chart = ChartGenerator()

        chart.performance_trend(

            scores

        )

        st.image(

            "assets/charts/performance.png"

        )

        st.metric(

            "Improvement",

            f"{analyzer.improvement(interviews)} %"

        )