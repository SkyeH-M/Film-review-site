from filmreview import db
from flask import Flask
from flask_login import (LoginManager, UserMixin, login_user, login_required,
                         logout_user, current_user)

app = Flask(__name__)

login_manager = LoginManager(app)
login_manager.init_app(app)
# below means user is redirected to login page if they try to access
# login restricted pages
login_manager.login_view = 'login'


class Users(UserMixin, db.Model):
    """ Schema for Users model for login/signup """
    # entire model is empty now
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.username


class Watch_list(db.Model):
    """ Schema for watchlists created by user """
    id = db.Column(db.Integer, primary_key=True)
    list_name = db.Column(db.String(50), unique=False, nullable=False)
    created_by = db.Column(db.String(50), nullable=True)
    # ref one to many relationship, not visible in database
    films = db.relationship("Film", backref="watch_list",
                            cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to rep itself in the form of a string
        return self.list_name


class Film(db.Model):
    """ Schema for films added to watchlist, or a review added """
    id = db.Column(db.Integer, primary_key=True)
    film_title = db.Column(db.String(50), unique=False, nullable=False)
    star_rating = db.Column(db.Integer, unique=False, nullable=False)
    written_review = db.Column(db.String(200), unique=False, nullable=True)
    watchlist_id = db.Column(db.Integer, db.ForeignKey("watch_list.id",
                             ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        return self.film_title
