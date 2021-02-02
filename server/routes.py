import flask
from server import app


@app.route("/")
def home():
    return flask.render_template("layout.html")
