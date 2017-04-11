from random import choice
from flask import Flask, request, redirect, url_for, abort, \
    render_template

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    SECRET_KEY='development key'
))

from foood import foooddata

def random_meals(n):
    '''Returns list of n random choices (no repeats) from list of all meals'''
    meals = []
    while len(meals) < (n):
        random_meal = choice(foooddata.meals)
        if random_meal not in meals:
            meals.append(random_meal)
    return meals

@app.route('/')
def show_meal():
    return render_template('meal.html', meal=random_meals(1)[0])

@app.route('/all')
def show_all():
    return render_template('all.html', meals=foooddata.meals)

@app.route('/planner/<number_of_meals>')
def show_plan(number_of_meals):
    return render_template('planner.html', meals=random_meals(int(number_of_meals)))

