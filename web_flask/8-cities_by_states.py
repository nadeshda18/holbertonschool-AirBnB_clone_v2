#!/usr/bin/python3
""" This module starts a Flask web application """""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
""" Flask class and render_template method"""""
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Display hello message

    Returns:
        str: hello message
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display HBNB

    Returns:
        str: HBNB
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Display text

    Args:
        text (str): text to display

    Returns:
        str: text
    """
    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Display other text

    Args:
        text (str, optional): Other text to display. Defaults to "is cool".

    Returns:
        str: text
    """
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Display number

    Args:
        n (int): number to display

    Returns:
        str: text with number
    """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Display HTML template

    Args:
        n (int): number to check

    Returns:
        str: HTML template
    """
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """Check if number is odd or even

    Args:
        n (int): number to check

    Returns:
        str: HTML template
    """
    return render_template("6-number_odd_or_even.html", n=n)


@app.route('/states_list', strict_slashes=False)
def states_list():
    states = storage.all('State').values()
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
def teardown_db(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
