from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    name = ""

    if request.method == "POST":
        name = request.form.get("username")
        score = 0

        if request.form.get("q1"):
            score += 2
        if request.form.get("q2"):
            score += 2
        if request.form.get("q3"):
            score += 2
        if request.form.get("q4"):
            score += 2

        if score <= 2:
            result = "Low Risk"
        elif score <= 6:
            result = "Medium Risk"
        else:
            result = "High Risk"

        with open("result.txt", "a", encoding="utf-8") as f:
            f.write(f"Name: {name} | Risk: {result}\n")

    return render_template("index.html", result=result, name=name)

if __name__ == "__main__":
    app.run(debug=True)
