from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    name = request.form["username"]
    mood = request.form["mood"]
    language = request.form["language"]
    age = int(request.form["age"])

    if age < 18:
        age_message = "Вы начинающий разработчик — самое время учиться новому!"
    else:
        age_message = "Отличный возраст, чтобы собирать собственное портфолио!"

    return render_template(
        "result.html",
        name=name,
        mood=mood,
        language=language,
        age_message=age_message
    )

if __name__ == "__main__":
    app.run(debug=True)

