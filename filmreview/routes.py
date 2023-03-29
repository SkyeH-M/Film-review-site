from flask import render_template
from filmreview import app, db
from filmreview.models import Watch_list  # Users removed from here?
# below is from Pretty Printed, User Login with Flask-Login
# installed flaskwtf with pip install -U Flask-WTF
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length


# below is from Pretty Printed flask login
class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(
    ), Length(min=4, max=20)])
    password = PasswordField('password', validators=[InputRequired(
    ), Length(min=5, max=80)])
    remember = BooleanField('remember me')


class RegisterForm(FlaskForm):
    email = StringField('email', validators=[
        InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(
    ), Length(min=4, max=20)])
    password = PasswordField('password', validators=[InputRequired(
    ), Length(min=5, max=80)])


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/search")
def search():
    return render_template("search.html")


@app.route("/add_film", methods=["GET", "POST"])
def add_film():
    return render_template("add_film.html")


@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", form=form)


@app.route("/signup")
def signup():
    form = RegisterForm()
    return render_template("signup.html", form=form)
