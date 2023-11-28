import os
from flask import Flask, render_template
from flask_sitemap import Sitemap

app = Flask(__name__)
sitemap = Sitemap(app=app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/gcse-english.html")
def gcse_english():
    return render_template("gcse-english.html")


@app.route("/notebooks.html")
def notebooks():
    return render_template("notebooks.html")


@app.route("/articles")
def articles():
    return render_template("articles.html")


@app.route("/unleasing-creativity.html")
def creativity():
    return render_template("unleasing-creativity.html")


@app.route("/memoir-stories.html")
def stories():
    return render_template("memoir-stories.html")


@app.route("/memory-memoir.html")
def memoir():
    return render_template("memory-memoir.html")


@app.route("/paperback-notebooks.html")
def paperback_notebooks():
    return render_template("paperback-notebooks.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)


@app.route('/sitemap.xml')
def sitemap_xml():
    return sitemap.sitemap(), 200, {'Content-Type': 'application/xml'}


