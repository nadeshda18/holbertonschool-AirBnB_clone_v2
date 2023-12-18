#!/usr/bin/python3
"""Start a Flask web app"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from os import environ

app = Flask(__name__)


@app.route('/hbnb_filters')
def hbnb_filters():
    """
    Display a HTML page like 6-index.html, but with a filters box

    Returns:
        HTML: HTML page with list of all City objects
    """
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()

    if environ.get('HBNB_TYPE_STORAGE') == 'db':
        cities = storage.all(City).values()
    else:
        cities = {}

    dropdown_data = [{'value': state.id, 'label': state.name}
                     for state in states]

    return render_template('10-hbnb_filters.html', states=states, cities=cities, amenities=amenities, dropdown_data=dropdown_data)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
