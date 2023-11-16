import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/gcse-english")
def about():
    return render_template("gcse-english.html")


@app.route("/paperback-notebooks")
def about():
    return render_template("paperback-notebooks.html")


@app.route("/articles.html")
def blog():
    return render_template("articles.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)