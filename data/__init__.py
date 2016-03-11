from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

from .schema import *        # noqa

@app.route("/")
def index():
    return ""
