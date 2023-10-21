#!/usr/bin/python3
"""Defines a Flask web app

Attribtes:
    app (obj): Instance of the Flask class
"""

from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route("/")
def root_route():
    """Renders text

    Returns:
        String to page
    """
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    """Renders text

    Returns:
        String to page
    """
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """Renders text

    Returns:
        String to page
    """
    if '_' in text:
        text = text.replace('_', ' ')
    return f'C {escape(text)}'


@app.route("/python", strict_slashes=False)
@app.route("/python/<path:text>", strict_slashes=False)
def python_route(text='is cool'):
    """Renders text

    Returns:
        String to page with custome text or with default
        text
    """
    if '_' in text:
        text = text.replace('_', ' ')
    return f'Python {escape(text)}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
