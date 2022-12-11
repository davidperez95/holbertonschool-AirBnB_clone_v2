#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
from models.state import State
from models import storage
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """display the states and cities listed in alphabetical order"""
    states = storage.all(State)
    if id is not None:
        state_id = 'State.' + id
        return render_template('9-states.html', states=states, state_id=state_id)
    else:
        return render_template('9-states.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')