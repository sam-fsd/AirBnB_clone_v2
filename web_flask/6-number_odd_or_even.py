#!/usr/bin/python3
"""Defines a Flask web app

Attribtes:
    app (obj): Instance of the Flask class
"""

from flask import Flask, render_template
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


@app.route("/number/<int:n>")
def number_route(n):
    """Display number only if n is an integer"""
    return f"{escape(n)} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Renders a template if n is a positive integer"""
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """ display a HTML page only if n is an intege"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
