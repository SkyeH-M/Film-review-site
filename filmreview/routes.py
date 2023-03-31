# Bugs
# 1) FIX- registerform works to return h1 but loginform does not-
# 1) didn't include form.hidden_tag() on login!


from flask import render_template, request
# installed flask-bootstrap with 'pip install flask-bootstrap'
# from flask_bootstrap import Bootstrap
from filmreview import app, db
from filmreview.models import Watch_list, Users
# below from Pretty Printed
from flask_bootstrap import Bootstrap4
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length

# below from Pretty Printed
bootstrap = Bootstrap4(app)


class LoginForm(FlaskForm):
    username = StringField("username", validators=[InputRequired(
    ), Length(min=4, max=20)])
    password = PasswordField("password", validators=[InputRequired(
    ), Length(min=5, max=80)])
    remember = BooleanField("remember me")


class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(
        message='Invalid email'), Length(max=50)])
    username = StringField("username", validators=[InputRequired(
    ), Length(min=4, max=20)])
    password = PasswordField("password", validators=[InputRequired(
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


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    # has form been submit? if yes continue, if no render_template
    if request.method == 'POST' and form.validate_on_submit():
        return f"<h1> {form.username.data}, {form.password.data} </h1>"
    return render_template("login.html", form=form)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = RegisterForm()
    if request.method == 'POST' and form.validate_on_submit():
        new_user = Users(
            username=form.username.data, email=form.email.data,
            password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return '<h1> New user has been created </h1>'
        # return f"<h1> {usernameData}, {emailData},
        #  {form.password.data} </h1>"
    return render_template("signup.html", form=form)
