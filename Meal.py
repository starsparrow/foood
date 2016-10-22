#!/usr/bin/env python

class Meal:
	'''What you should eat. Composed of one or more Recipes.'''
	def __init__(self):
		self.dishes = {
			"entree": "",
			"sides": []
		}

	def add_entree(self, dish):
		self.dishes["entree"] = dish

	def add_side(self, dish):
		self.dishes["sides"].append(dish)

	def get_data(self):
		return self.dishes

	def print_data(self):
		data = self.get_data()
		print("Entree: {0}".format(data["entree"]))
		i = 1
		for side in data["sides"]:
			print("Side {0}: {1}".format(str(i), side))
			i += 1