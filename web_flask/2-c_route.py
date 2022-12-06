#!/usr/bin/python3
"""
This module start the conection with flask,
for conect the web con database
"""
from flask import Flask


app = Flask(__name__)


@app.route('/')
def slash():
    """This method return the messege of the page /"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """This method return other page"""
    return "HBNB"


@app.route('/c')
@app.route('/c/<text>')
def c(text=None):
    """This method return the text if exist the param"""
    if text is not None:
        text = text.replace("_", " ")
        return f"C {text}"
    return "C is funny"


if __name__ == '__main__':
    app.run(debug=True, port=5000)