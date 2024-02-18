#!/usr/bin/python3
<<<<<<< HEAD
""" Starts a Flask web Application"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Returns a string to the root route /"""
    return "Hello HBNB"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns a string to the root route /hbnb"""
=======
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB'."""
>>>>>>> a1a68afd0dca7866b0e2a5e292f4e0a52be6468c
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
