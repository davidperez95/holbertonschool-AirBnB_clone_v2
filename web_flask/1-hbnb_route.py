#!/usr/bin/python3
"""
This script display “Hello HBNB!” on '/' and
“HBNB” on /hbnb route
"""
from flask import Flask


app = Flask(__name__)


@app.route('/')
def main_page():
    """Return “Hello HBNB!” on the console"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """Return "HBNB" on the console on /hbnb"""
    return "HBNB"


if __name__ == '__main__':
    app.run(debug=True, port=5000)
