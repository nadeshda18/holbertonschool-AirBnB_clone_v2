#!/usr/bin/python3
""" This module starts a Flask web application """""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
""" Flask class and render_template method"""""
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
