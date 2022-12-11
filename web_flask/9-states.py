#!/usr/bin/python3
"""
Starts a flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """Display a list of all states on a html page"""
    states = storage.all(State)
    return render_template('9-states.html', state=states)

@app.route("/states/<id>")
def states_id(id):
    """Display an state acording with id"""
    for state in storage.all(State).values():
        if state.id == id:
            return render_template('9-states.html', state=state)
    return render_template('9-states.html')


@app.teardown_appcontext
def teardown_db(exeption):
    """remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
