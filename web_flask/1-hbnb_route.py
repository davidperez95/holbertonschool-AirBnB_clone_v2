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


if __name__ == '__main__':
    app.run(debug=True, port=5000)
