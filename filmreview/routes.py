# Bugs
# 1) FIX- registerform works to return h1 but loginform does not-
# 1) didn't include form.hidden_tag() on login!


from flask import render_template, request, redirect, url_for, flash
# installed flask-bootstrap with 'pip install flask-bootstrap'
# from flask_bootstrap import Bootstrap
from filmreview import app, db
from filmreview.models import Watch_list, Users
# below from Pretty Printed
from flask_bootstrap import Bootstrap4
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from werkzeug.security import generate_password_hash, check_password_hash
# is the indentation below an issue?
from flask_login import (LoginManager, UserMixin, login_user, login_required,
                         logout_user, current_user)

# below from Pretty Printed
bootstrap = Bootstrap4(app)

login_manager = LoginManager(app)
login_manager.init_app(app)
# below means user is redirected to login page if they try to access
# login restricted pages
login_manager.login_view = 'login'
login_manager.login_message = 'Please sign up or login to view this page'


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


class LoginForm(FlaskForm):
    username = StringField("username", validators=[InputRequired(
    ), Length(min=4, max=20)])
    password = PasswordField("password", validators=[InputRequired(
    ), Length(min=5, max=80)])


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
@login_required
def search():
    return render_template("search.html", name=current_user.username)


@app.route("/add_film", methods=["GET", "POST"])
@login_required
def add_film():
    return render_template("add_film.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    # has form been submit? if yes continue, if no render_template
    if request.method == 'POST' and form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                # signs user in, can now access loginRequired pages
                login_user(user)
                # this redirect will be changed to films
                return redirect(url_for('search'))
            else:
                flash('Wrong username or password, please try again', 'error')
            return redirect(url_for('login'))
        else:
            flash("User doesn't exist, please Sign Up", "error")
            return redirect(url_for('signup'))
    return render_template("login.html", form=form)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = RegisterForm()
    if request.method == 'POST' and form.validate_on_submit():
        # generate hash that is 80 char in length
        hashed_password = generate_password_hash(
            form.password.data, method='sha256', salt_length=8)

        new_user = Users(
            username=form.username.data, email=form.email.data,
            password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        if new_user:
            flash("Thank you for registering", 'message')
            return redirect(url_for('home'))

        # return f"<h1> {usernameData}, {emailData},
        #  {form.password.data} </h1>"
    return render_template("signup.html", form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out', 'message')
    return redirect(url_for('home'))
# delete first database record for Users as password is not yet hashed
# Users.query.filter_by(id=1).delete()
# db.session.commit()
