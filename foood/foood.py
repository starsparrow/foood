from random import choice
from flask import Flask, request, redirect, url_for, abort, \
    render_template

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    SECRET_KEY='development key'
))

from foood import foooddata

@app.route('/')
def show_meal():
    return render_template('meal.html', meal=choice(foooddata.meals))

@app.route('/all')
def show_all():
    return render_template('all.html', meals=foooddata.meals)

