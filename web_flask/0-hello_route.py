#!/usr/bin/python3
"""Starts a Flask web app"""

from flask import Flask

# create an instance of the Flask class
app = Flask(__name__)

# strict_slashes=False in your route definition
# define the route for the root URL


@app.route('/', strict_slashes=False)
def hello():
    # functin to be executed when the root URL is accessed
    return 'Hello HBNB!'


# check if the script is run directly and not imported
if __name__ == '__main__':
    # start the Flask web server host 0.0.0.0 and port 5000
    app.run(host='0.0.0.0', port=5000)
