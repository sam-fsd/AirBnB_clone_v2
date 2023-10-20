#!/usr/bin/python3
"""Defines a Flask function"""

from flask import Flask


app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello():
    """ Runs when the route is accessd

    Returns:
        String. A text to display
    """
    return f'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
