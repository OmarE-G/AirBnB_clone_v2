"""simple app"""
from flask import Flask


app = Flask(__name__)

app.url_map.strict_slashes = False


@app.route('/')
def Hello():
    return "Hello HBNB!"
