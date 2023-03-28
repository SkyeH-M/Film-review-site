from flask import render_template
from filmreview import app, db
from filmreview.models import Users, Watch_list


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/search")
def search():
    return render_template("search.html")


@app.route("/add_film", methods=["GET", "POST"])
def add_film():
    return render_template("add_film.html")
