import re


def extract_projects(text):

    projects = []

    keywords = [

        "project",
        "developed",
        "built",
        "implemented"

    ]

    lines = text.split("\n")

    for line in lines:

        for key in keywords:

            if key.lower() in line.lower():

                projects.append(line)

                break

    return projects