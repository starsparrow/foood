#!/usr/bin/env python

from datetime import datetime

class Recipe:
	def __init__(self, name):
		self.name = name
		self.ingredients = []
		self.weight = ''
		self.eatcount = 0
		self.lasteaten = 'Never'
		self.notes = ''
		self.tags = []

	def load():
		'''Reads the recipe from the database'''
		pass

	def save():
		'''Writes the recipe to the database'''
		pass

	def eat():
		'''Update stats when this item is chosen for a meal'''
		self.eatcount += 1
		self.lasteaten = datetime.now()

	def set_note(note):
		'''Updates the note on file for the recipe'''
		self.notes = note

	def set_name(name):
		'''Updates the name of the recipe'''
		self.name = name

	def set_ingredients(ingredients):
		'''Updates the things that go into the recipe'''
		self.ingredients = ingredients

	def set_weight(weight):
		'''Updates the weight of the recipe'''
		self.weight = weight

	def add_tag(tag):
		'''Adds a tag to the recipe'''
		self.tags.append(tag)

	def remove_tag(tag):
		'''Removes a tag from the recipe'''
		self.tags.delete(tag)
