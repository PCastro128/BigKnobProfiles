from flask import Flask

PORT = 5001

app = Flask(__name__)
from source.server import routes


def start():
    app.run(host="localhost", port=PORT)
