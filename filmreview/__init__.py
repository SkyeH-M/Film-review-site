import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")


db = SQLAlchemy(app)  # removed app from ()
# db.drop_all()
# db.create_all()


# db.init_app(app)

# with app.app_context():
#     from . import routes  # Import routes
#     db.create_all()  # Create sql tables for our data models

# # return app

from filmreview import routes  # noqa
