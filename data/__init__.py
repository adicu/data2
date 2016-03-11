from flask import Flask, render_template, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask.ext.assets import Environment, Bundle

app = Flask(__name__)
db = SQLAlchemy(app)
assets = Environment(app)
assets.url = app.static_url_path
scss = Bundle('../assets/app.scss', filters='scss', output='app.css')
assets.register('scss_all', scss)

from .schema import *        # noqa

@app.route("/")
def index():
    return render_template('hello.html')
