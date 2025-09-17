from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def student():
    return render_template(
        "profile.html",
        name="Korim",
        is_topper = "True",
        subjects = ["Math", "Physics", "Chemistry"]
        
    )