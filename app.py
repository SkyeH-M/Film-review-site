# Unorganised file, concerned with login/signup functionality
# I wanted to keep this file separate and not put classes into routes.py
# but variables kept showing undefined so I've put them into routes.py
# Pretty Printed- User Login System with Flask-Login

from flask import Flask, render_template
# from here this is pretty printed imports
# from flask_bootstrap import Bootstrap4
# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, BooleanField
# from wtforms.validators import InputRequired, Email, Length


# app = Flask(__name__)
# bootstrap = Bootstrap4(app)


# class LoginForm(FlaskForm):
#     username = StringField("username", validators=[InputRequired(
#     ), Length(min=4, max=15)])
#     password = PasswordField("password", validators=[InputRequired(
#     ), Length(min=5, max=80)])
#     remember = BooleanField("remember me")


# class RegisterForm(FlaskForm):
#     email = StringField('email', validators=[InputRequired(), Email(
#         message='Invalid email'), Length(max=50)])
#     username = StringField("username", validators=[InputRequired(
#     ), Length(min=4, max=15)])
#     password = PasswordField("password", validators=[InputRequired(
#     ), Length(min=5, max=80)])
#     remember = BooleanField("remember me")


# @app.route("/")
# def home():
#     return render_template("index.html")


# @app.route("/search")
# def search():
#     return render_template("search.html")


# @app.route("/add_film", methods=["GET", "POST"])
# def add_film():
#     return render_template("add_film.html")


# @app.route("/login", methods=["GET", "POST"])
# def login():
#     form = LoginForm()
#     return render_template("login.html", form=form)


# @app.route("/signup", methods=["GET", "POST"])
# def signup():
#     form = RegisterForm()
#     return render_template("signup.html", form=form)


# if __name__ == '__main__':
#     app.run(debug=True)
