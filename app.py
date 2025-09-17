from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def landing():
    return render_template("landing.html")

@app.route("/profile")
def student_profile():
    return render_template(
        "studentProfile.html",
        name="Korim",
        is_topper = True,
        subjects = ["Maths", "Physics", "Chemistry"]
    )