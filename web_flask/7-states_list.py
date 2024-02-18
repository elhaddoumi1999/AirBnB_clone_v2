#!/usr/bin/python3
"""
starts a Flask web application
manipulates storage
"""
from models import storage
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """
    Displays a html page with a list of all state objects
    in DBStorage
    """
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """
    Removes the current SQLAlchemy session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
