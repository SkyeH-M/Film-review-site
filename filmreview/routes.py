from flask import render_template
from filmreview import app, db
from filmreview.models import Users, Watch_list


@app.route("/")
def home():
    return render_template("base.html")
