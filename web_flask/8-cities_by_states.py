#!/usr/bin/python3
""" This script that starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/states_list')
def states_list():
    """display html page
       fetch sorted states to insert into html in UL tag
    """
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states')
def cities_by_states():
    """display a HTML page with list of all State objects and their cities"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    for state in states:
        state.cities = sorted(state.cities, key=lambda city: city.name)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown(exception):
    """Closes the storage on teardown."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
