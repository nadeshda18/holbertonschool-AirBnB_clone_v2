#!/usr/bin/python3
"""
Script that starts a Flask web application
"""


from flask import Flask


# Create a Flask web application instance
app = Flask(__name__)

# Define a route for the root URL ("/") and disable strict_slashes
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route handler for the root URL ("/")
    """
    return 'Hello HBNB!'

# Check if the script is being run directly
if __name__ == '__main__':
    # Run the Flask web application on 0.0.0.0 (all available network interfaces) on port 5000
    app.run(host='0.0.0.0', port=5000)
