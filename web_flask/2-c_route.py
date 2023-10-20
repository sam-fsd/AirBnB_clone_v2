#!/usr/bin/python3
"""Defines a Flask web app

Attribtes:
    app (obj): Instance of the Flask class
"""

from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """Renders text
    
    Returns:
        String to page
    """
    if '_' in text:
        text = text.replace('_', ' ')
    return f'C {escape(text)}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
