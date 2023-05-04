# Bugs
# 1) FIX- registerform works to return h1 but loginform does not-
# 1) didn't include form.hidden_tag() on login!
# How to get Bootstrap custom select via models.py for genre?


from flask import render_template, request, redirect, url_for, flash, session
# installed flask-bootstrap with 'pip install flask-bootstrap'
from filmreview import app, db, os
from filmreview.models import Watch_list, Users, Film
# below from Pretty Printed
from flask_bootstrap import Bootstrap4
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import InputRequired, Email, Length
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import (LoginManager, UserMixin, login_user, login_required,
                         logout_user, current_user)
import requests
import json

# below from Pretty Printed
bootstrap = Bootstrap4(app)

login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Please sign up or login to view this page'
api_key = os.environ.get("API_KEY")


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


class SearchForm(FlaskForm):
    searched = StringField('Searched', validators=[InputRequired()])
    submit = SubmitField("Submit")


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


@app.route("/search", methods=["GET", "POST"])
@login_required
def search():
    form = SearchForm()
    if request.method == "POST":
        """
        Makes sense youtube API calls to MovieDb
        Connect to API, retrieve film title, description, and image data
        Post returned API data to search.html film
        """

        moviedb_base_url = "https://api.themoviedb.org/3"

        def load_json_for_url(url):
            response = requests.get(url)
            return json.loads(response.text)

        def load_moviedb_info(movie_title):
            movie_title = movie_title.replace(" ", "+").lower()
            api_written_data = load_json_for_url(
                f"{moviedb_base_url}/search/movie?api_key={api_key}"
                f"&query={movie_title}")

            return api_written_data['results']

        movie_title = request.form.get("search")

        data = load_moviedb_info(movie_title)
        session["data"] = data
        # if film doesn't exist in api database...
        if len(data) == 0:
            flash(f"Unfortunately we can't find a film with"
                  f" the title, '{movie_title}' please choose another")
        else:
            return render_template("search.html", form=form, data=data,
                                   search_string=movie_title,
                                   name=current_user.username)
    return render_template("search.html", name=current_user.username)


@app.route("/watchlists")
@login_required
def watchlists():
    watchlists = list(Watch_list.query.order_by(Watch_list.list_name).all())
    return render_template("watchlists.html", watchlists=watchlists)


@app.route("/add_watchlist", methods=["GET", "POST"])
@login_required
def add_watchlist():
    if request.method == "POST":
        watchlist = Watch_list(list_name=request.form.get("list_name"),
                               created_by=current_user.username,
                               genre=request.form.get("genre"))
        db.session.add(watchlist)
        db.session.commit()
        flash("Your Film List has been successfully created")
        return redirect(url_for("watchlists"))
    return render_template("add_watchlist.html")


@app.route("/edit_watchlist/<int:watchlist_id>", methods=["GET", "POST"])
@login_required
def edit_watchlist(watchlist_id):
    watchlist = Watch_list.query.get_or_404(watchlist_id)
    if current_user.username != watchlist.created_by:
        flash("You cannot edit another user's list")
        return redirect(url_for('watchlists'))

    if (request.method == 'POST' and current_user.username
            == watchlist.created_by):
        watchlist.list_name = request.form.get("list_name")
        watchlist.created_by = current_user.username
        watchlist.genre = request.form.get("genre")
        db.session.commit()
        flash("Your film list was edited successfully")
        return redirect(url_for("watchlists"))
    return render_template("edit_watchlist.html", watchlist=watchlist)


@app.route("/delete_watchlist/<int:watchlist_id>")
@login_required
def delete_watchlist(watchlist_id):
    watchlist = Watch_list.query.get_or_404(watchlist_id)
    if current_user.username != watchlist.created_by:
        flash("You cannot delete another user's list")
        return redirect(url_for('watchlists'))

    if current_user.username == watchlist.created_by:
        db.session.delete(watchlist)
        db.session.commit()
        flash("Your film list has been deleted")
    return redirect(url_for("watchlists"))


@app.route("/add_film", methods=["GET", "POST"])
@login_required
def add_film():
    watchlists = list(Watch_list.query.order_by(Watch_list.list_name).all())
    try:
        if request.method == "POST" and len(watchlists) != 0:
            film = Film(
                id=request.form.get("id"),
                reviewed_by=current_user.username,
                film_title=request.form.get("film_title"),
                star_rating=request.form.get("rating"),
                written_review=request.form.get("writtenReview"),
                watchlist_id=request.form.get("watchlist_id")
            )
            db.session.add(film)
            db.session.commit()
            flash("You review has been added successfully")
            return redirect(url_for("films"))

    # if film list doesn't already exist
    except Exception:
        flash("Please create a Film List before adding reviews")
        return redirect(url_for('add_watchlist'))

    return render_template("add_film.html", watchlists=watchlists)


@app.route("/films")
@login_required
def films():
    films = list(Film.query.order_by(Film.id).all())
    return render_template("films.html", films=films)


@app.route("/edit_film/<int:film_id>", methods=["GET", "POST"])
@login_required
def edit_film(film_id):
    film = Film.query.get_or_404(film_id)
    watchlists = list(Watch_list.query.order_by(Watch_list.list_name).all())
    if request.method == "POST":
        film.film_title = request.form.get("film_title")
        film.star_rating = request.form.get("rating")
        film.written_review = request.form.get("writtenReview")
        film.watchlist_id = request.form.get("watchlist_id")
        # determine if user has not selected a watchlist
        if film.watchlist_id == "Choose your Film List":
            flash("Please choose a film list for your review")
        else:
            db.session.commit()
            flash("Your review has been updated")
            return redirect(url_for('films'))
    return render_template("edit_film.html", film=film, watchlists=watchlists)


@app.route("/delete_film/<int:film_id>")
@login_required
def delete_film(film_id):
    film = Film.query.get_or_404(film_id)
    if film.reviewed_by != current_user.username:
        flash("You cannot delete another user's review")
        return redirect(url_for('films'))

    if film.reviewed_by == current_user.username:
        db.session.delete(film)
        db.session.commit()
        flash("Your film review has been deleted")
    return redirect(url_for("films"))


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
                flash("You've been logged in")
                return redirect(url_for('search'))
        else:
            flash('Wrong username or password, please try again')
            return redirect(url_for('login'))
    return render_template("login.html", form=form)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = RegisterForm()
    if request.method == 'POST' and form.validate_on_submit():
        # generate hash that is 80 char in length
        existing_username = Users.query.filter(Users.username == request.form
                                               .get("username").lower()).all()
        if existing_username:
            flash("This username has already been taken, "
                  "please choose another")
            return redirect(url_for('signup'))

        existing_email = Users.query.filter(Users.email == request.form
                                            .get("email").lower()).all()
        if existing_email:
            flash("This email already exists, please log in to your account")
            return redirect(url_for("login"))

        hashed_password = generate_password_hash(
            form.password.data, method='sha256', salt_length=8)
        new_user = Users(
            username=form.username.data, email=form.email.data,
            password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        if new_user:
            flash("Thank you for registering", 'message')
            return redirect(url_for('login'))

    return render_template("signup.html", form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out', 'message')
    return redirect(url_for('home'))
