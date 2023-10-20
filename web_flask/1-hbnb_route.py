#!/usr/bin/python3
"""Define Flask Web app"
Attributes:
    app(obj): Instance of Flask class
"""

from flask import Flask


app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    """Defines a hbnb route
    Returns:
        Display text
    """
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
