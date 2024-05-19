#!/usr/bin/python3
"""simple app"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Hello():
    """say hello"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """say hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def ctext(text):
    """say c is text"""
    return "C " + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
