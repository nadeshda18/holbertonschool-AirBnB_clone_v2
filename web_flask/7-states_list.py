#!/usr/bin/python3
"""
starts a Flask web application listening on
0.0.0.0, port 5000 and routes /: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display "C" + text (replaces underscores with spaces)
/python/(<text>): display "Python" + text (default is 'is cool')
/number/<n>: display "n is a number" only if n is an integer
/number_template/<n>: display HTML page only if n is an integer
/number_odd_or_even/<n>: display HTML page only if n is an integer
/state_list: display HTML page with list of all State objects
"""
from flask import Flask, render_template
from models import storage
from models.state import State
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


@app.teardown_appcontext
def teardown_db(exception):
    """Close the db connection

    Args:
        exception (str): exception to close
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    states = storage.all('State').values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
