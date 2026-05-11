def generate_ai_feedback(text):
    feedback = []

    text_lower = text.lower()

    if "project" not in text_lower:
        feedback.append("Add real-world projects with tech stack and impact.")

    if "python" not in text_lower and "java" not in text_lower:
        feedback.append("Include technical skills like Python, Java, or frameworks.")

    if "intern" not in text_lower:
        feedback.append("Add internships or practical experience.")

    if len(text.split()) < 120:
        feedback.append("Expand resume with more details and achievements.")

    feedback.append("Use measurable impact (e.g., improved performance by 20%).")

    return feedback


def ats_score(text):
    score = 50
    text_lower = text.lower()

    if "project" in text_lower:
        score += 15
    if "python" in text_lower:
        score += 10
    if "experience" in text_lower or "intern" in text_lower:
        score += 10
    if len(text.split()) > 150:
        score += 10

    return min(score, 100)