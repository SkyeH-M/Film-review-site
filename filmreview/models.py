from filmreview import db


class Users(db.Model):
    """ Schema for Users model for login/signup """
    # entire model is empty now
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        # __repr__ to rep itself in the form of a string
        return self.username


class Watch_list(db.Model):
    """ Schema for films reviewed by user """
    # watch list is also empty
    id = db.Column(db.Integer, primary_key=True)
    list_name = db.Column(db.String(50), unique=False, nullable=False)
    created_by = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        # __repr__ to rep itself in the form of a string
        return self.list_name
