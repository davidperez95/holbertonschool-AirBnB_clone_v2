#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)

@app.route('/')
def slash():
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(debug=True, port=5000)