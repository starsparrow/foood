#!/usr/bin/env python
from Recipe import Recipe

blah = Recipe('dish')

blah.print_recipe()

blah.set_name('dish2')
blah.eat()
blah.set_ingredients(['onion','potato','lentils','curry sauce'])
blah.set_weight('green')
blah.add_tag('lol what')
blah.set_note('this was good')

blah.print_recipe()