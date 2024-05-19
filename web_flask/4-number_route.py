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


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pytext(text="is cool"):
    """say py is text"""
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    """say num"""
    if type(n) is int:
        return str(n) + " is a number"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
