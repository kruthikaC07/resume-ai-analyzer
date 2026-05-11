from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# ---------------- HOME ROUTE ----------------
@app.route("/")
def home():
    return "🚀 AI Resume Analyzer Backend Running"


# ---------------- AI FEEDBACK FUNCTION ----------------
def generate_ai_feedback(text):

    feedback = []

    text_lower = text.lower()

    # Projects
    if "project" not in text_lower:
        feedback.append(
            "Add real-world projects with technologies used and outcomes."
        )

    # Skills
    if (
        "python" not in text_lower
        and "java" not in text_lower
        and "c" not in text_lower
        and "javascript" not in text_lower
    ):
        feedback.append(
            "Add technical skills like Python, Java, C, or JavaScript."
        )

    # Experience
    if (
        "internship" not in text_lower
        and "experience" not in text_lower
    ):
        feedback.append(
            "Include internships, freelance work, or practical experience."
        )

    # Education
    if "education" not in text_lower:
        feedback.append(
            "Add an Education section."
        )

    # Skills section
    if "skills" not in text_lower:
        feedback.append(
            "Include a dedicated Skills section."
        )

    # Resume size
    if len(text.split()) < 100:
        feedback.append(
            "Resume is too short. Add more details about projects, skills, and achievements."
        )

    # LinkedIn
    if "linkedin" not in text_lower:
        feedback.append(
            "Add your LinkedIn profile for better professional visibility."
        )

    # GitHub
    if "github" not in text_lower:
        feedback.append(
            "Add your GitHub profile to showcase technical work."
        )

    # Always useful suggestion
    feedback.append(
        "Use measurable achievements like 'Improved performance by 20%'."
    )

    return feedback


# ---------------- ATS SCORE FUNCTION ----------------
def ats_score(text):

    score = 40

    text_lower = text.lower()

    # Projects
    if "project" in text_lower:
        score += 15

    # Technical Skills
    if (
        "python" in text_lower
        or "java" in text_lower
        or "c" in text_lower
        or "javascript" in text_lower
    ):
        score += 15

    # Experience
    if (
        "experience" in text_lower
        or "internship" in text_lower
    ):
        score += 10

    # Education
    if "education" in text_lower:
        score += 5

    # Skills section
    if "skills" in text_lower:
        score += 5

    # LinkedIn
    if "linkedin" in text_lower:
        score += 5

    # GitHub
    if "github" in text_lower:
        score += 5

    # Resume length
    if len(text.split()) > 150:
        score += 10

    return min(score, 100)


# ---------------- ANALYZE RESUME ----------------
@app.route("/analyze-text", methods=["POST"])
def analyze_text():

    try:

        data = request.get_json()

        resume_text = data.get("resume", "")

        if resume_text.strip() == "":

            return jsonify({
                "score": 0,
                "feedback": [
                    "Please paste your resume text."
                ]
            })

        feedback = generate_ai_feedback(resume_text)

        score = ats_score(resume_text)

        return jsonify({
            "score": score,
            "feedback": feedback
        })

    except Exception as e:

        print("ERROR:", str(e))

        return jsonify({
            "score": 0,
            "feedback": [str(e)]
        })


# ---------------- MAIN ----------------
if __name__ == "__main__":

    print("🚀 Server running on http://127.0.0.1:5000")

    app.run(debug=True)