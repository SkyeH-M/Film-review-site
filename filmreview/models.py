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
    """ Schema for films added to watchlist by user """
    id = db.Column(db.Integer, primary_key=True)
    list_name = db.Column(db.String(50), unique=False, nullable=False)
    created_by = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        # __repr__ to rep itself in the form of a string
        return self.list_name

# I think using API means I don't need a Films model
# class Films(db.Model):
#     """ Schema for films searched for """
#     name = db.Column(db.String(), primary_key=True)
#     description = db.Column(db.String())
#     average_rating = db.Colum(db.Integer())
