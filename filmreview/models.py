from filmreview import db
# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, BooleanField
# from wtforms.validators import InputRequired, Email, Length


# class Users(db.Model):
#     """ Schema for Users model for login/signup """
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(25), unique=True, nullable=False)
#     password = db.Column(db.String, unique=False, nullable=False)

#     def __repr__(self):
#         # __repr__ to rep itself in the form of a string
#         return self.username


class Watch_list(db.Model):
    """ Schema for films reviewed by user """
    id = db.Column(db.Integer, primary_key=True)
    list_name = db.Column(db.String(50), unique=False, nullable=False)
    created_by = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        # __repr__ to rep itself in the form of a string
        return self.list_name


# # below is from Pretty Printed flask login
# class LoginForm(FlaskForm):
#     username = StringField('username', validators=[InputRequired(
#     ), Length(min=4, max=20)])
#     password = PasswordField('password', validators=[InputRequired(
#     ), Length(min=5, max=80)])
#     remember = BooleanField('remember me')
