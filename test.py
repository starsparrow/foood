#!/usr/bin/env python
from Recipe import Recipe

blah = Recipe('dish')

print(blah.get_data())

blah.set_name('dish2')
blah.eat()
blah.set_ingredients(['onion','potato','lentils','curry sauce'])
blah.set_weight('green')
blah.add_tag('lol what')
blah.set_note('this was good')

print(blah.get_data())