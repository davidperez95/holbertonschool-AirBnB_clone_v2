#!/usr/bin/python3
"""
Starts a flask web application
This is a comment
For the documentation
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states_list():
    """Display a list of States on a HTML page"""
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


@app.route("/states/<id>", strict_slases=False)
def states_id(id=None):
    """Display an state acording with id"""
    state = storage.all(State)
    return render_template('9-states.html', state=state, id=id)


@app.teardown_appcontext
def teardown_db(exeption):
    """remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
