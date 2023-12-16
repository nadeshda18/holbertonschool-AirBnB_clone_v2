#!/usr/bin/python3
""" This script that starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    states = storage.all(State).values()
    states_sorted = sorted(states, key=lambda x: x.name)
    return render_template('cities_by_states.html', states=states_sorted)


@app.teardown_appcontext
def teardown(exception):
    """Closes the storage on teardown."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
