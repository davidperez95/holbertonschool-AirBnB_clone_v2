#!/usr/bin/python3
"""
This script display “Hello HBNB!” on '/' and
“HBNB” on /hbnb route
"C <text>" on /c/ rourte and the text variable
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


@app.route('/c/<text>')
def display_text(text):
    """Return "C" + <text> variable on /c/"""
    new_string = text
    if '_' in new_string:
        new_string = text.replace('_', ' ')
    return 'C {}'.format(new_string)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
