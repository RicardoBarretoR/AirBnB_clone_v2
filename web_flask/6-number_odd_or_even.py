#!/usr/bin/python3
"""start a Flask web application"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Function showing Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Function showing HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def DisplayC(text):
    """Function showing C and the text input"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def DisplayPython(text='is cool'):
    """Function showing Python and the text input
       and a decorator in case of the default value of text
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Function return a integer"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """display a HTML page only if n is an
       integer and if is odd or even
    """
    if n % 2 == 0:
        s = 'even'
    else:
        s = 'odd'

    return render_template('6-number_odd_or_even.html', n=n, s=s)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
