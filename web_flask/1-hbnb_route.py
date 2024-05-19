#!/usr/bin/python3
"""simple app"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Hello():
    """say hello"""
    return "Hello HBNB!"


@app.route('/', strict_slashes=False)
def Hello():
    """say hbnb"""
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
