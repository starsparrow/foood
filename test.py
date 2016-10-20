#!/usr/bin/env python
from Recipe import Recipe

blah = Recipe('Vegeable Curry')

blah.print_data()

blah.set_name('Vegetable Curry')
blah.set_ingredients(['rice', 'onion', 'potato', 'chickpeas', 'curry sauce'])
blah.set_weight('Hearty')
blah.add_tag('Indian', 'spicy', 'vegetarian')
blah.eat()
blah.set_note('This was delicious!!')



blah.print_data()