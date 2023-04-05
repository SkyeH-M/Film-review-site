import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
if os.path.exists("env.py"):
    import env


# app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")


db = SQLAlchemy()  # removed app from ()
# migrate = Migrate()


# def create_app():
#     app = Flask(__name__)
#     db.init_app(app)
#     migrate.init_app(app, db)
#     return app


from filmreview import routes  # noqa
