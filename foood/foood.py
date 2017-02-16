from random import choice
from flask import Flask, request, redirect, url_for, abort, \
    render_template

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    SECRET_KEY='development key'
))
app.config.from_envvar('FOOOD_SETTINGS', silent=True)

@app.route('/')
def show_meal():
    meal = choice([1,2,3])
    return render_template('meal.html', meal=meal)

@app.route('/all')
def show_all():
    return render_template('all.html', meals=meals)
