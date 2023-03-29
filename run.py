import os
# keep this?
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# up to here
from filmreview import app


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG"),
    )
