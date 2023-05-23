#!/usr/bin/python3
"""Starts a flask web application
web application must be listening on 0.0.0.0, port 5000
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Displays a string"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays a string"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def croute(text):
    """Displays value of the text variable"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def proute(text="is cool"):
    """Displays value of the text variable"""
    return "Python {}".format(text.replace("_", " "))
    

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
