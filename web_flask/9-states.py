#!/usr/bin/python3
"""Start a Flask web app"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    state = storage.get(State, id)
    if state is not None:
        state.cities = sorted(state.cities, key=lambda city: city.name)
    else:
        state = None
    return render_template('9-states.html', state=state)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
