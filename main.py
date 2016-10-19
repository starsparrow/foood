#!/usr/bin/env python

import sqlite3
import json

class Meal:
	"""What you should have for dinner"""
	def __init__(self):
		self.entree = ''
		self.side1 = ''
		self.side2 = ''

conn = sqlite3.connect('meals.db')

cursor = conn.execute("select name from sqlite_master where type='table' and name='entrees';")
for row in cursor:
	print(row[0])

conn.close()