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

	def load(self):
		'''Reads the recipe from the database'''
		pass

	def save(self):
		'''Writes the recipe to the database'''
		pass

	def eat(self):
		'''Update stats when this item is chosen for a meal'''
		self.eatcount += 1
		self.lasteaten = datetime.now()

	def set_note(self, note):
		'''Updates the note on file for the recipe'''
		self.notes = note

	def set_name(self, name):
		'''Updates the name of the recipe'''
		self.name = name

	def set_ingredients(self, ingredients):
		'''Updates the things that go into the recipe'''
		self.ingredients = ingredients

	def set_weight(self, weight):
		'''Updates the weight of the recipe'''
		self.weight = weight

	def add_tag(self, tag):
		'''Adds a tag to the recipe'''
		self.tags.append(tag)

	def remove_tag(self, tag):
		'''Removes a tag from the recipe'''
		self.tags.delete(tag)

	def get_data(self):
		'''Returns attributes in a dict'''
		data = {}
		data["name"] = self.name
		data["ingredients"] = self.ingredients
		data["weight"] = self.weight
		data["eatcount"] = self.eatcount
		data["lasteaten"] = str(self.lasteaten)
		data["notes"] = self.notes
		data["tags"] = self.tags
		return data