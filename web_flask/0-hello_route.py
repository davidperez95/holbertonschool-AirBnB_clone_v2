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


if __name__ == '__main__':
    app.run(debug=True, port=5000)
