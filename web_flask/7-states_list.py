#!/usr/bin/python3
"""Starts a flask web application
web application must be listening on 0.0.0.0, port 5000
"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Returns a json list of all states"""
    states = storage.all()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(self):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
