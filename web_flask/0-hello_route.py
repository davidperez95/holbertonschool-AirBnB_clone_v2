#!/usr/bin/python3
"""
This script display “Hello HBNB!” on a Flask app
on '/' route
"""
from flask import Flask


app = Flask(__name__)


@app.route('/')
def main_page():
    """Return “Hello HBNB!” on the console"""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(debug=True, port=5000)
