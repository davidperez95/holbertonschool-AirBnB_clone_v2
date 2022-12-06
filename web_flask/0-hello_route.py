#!/usr/bin/python3
from flask import Flask
"""
This module start the conection with flask,
for conect the web con database
"""

app = Flask(__name__)


@app.route('/')
def slash():
    """This method return the messege of the page /"""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(debug=True, port=5000)
