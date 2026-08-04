def calculate_ats(profile):

    score = 0

    if profile["name"]:
        score += 10

    if profile["email"]:
        score += 10

    if profile["phone"]:
        score += 10

    score += min(len(profile["skills"]) * 5, 30)

    score += min(len(profile["projects"]) * 5, 20)

    score += min(len(profile["certifications"]) * 2, 10)

    score += min(len(profile["education"]) * 5, 10)

    return min(score, 100)