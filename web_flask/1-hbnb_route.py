#!/usr/bin/python3
"""
This module start the conection with flask,
for conect the web con database
"""
from flask import Flask


app = Flask(__name__)


@app.route('/')
@app.route('/hbnb')
def slash(hbnb=None):
    """This method return the messege of the page /"""
    if hbnb == None:
        return "Hello HBNB!"
    return "HBNB"



if __name__ == '__main__':
    app.run(debug=True, port=5000)
