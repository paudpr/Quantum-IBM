from datetime import datetime

class Book:
	def __init__(self, name, last_update, creation_date, recipes_list):
		if not isinstance(name, str):
			print("Name must be a string")
			exit()
		self.name = name
		self.last_update = datetime.now()
		self.creation_date = datetime.now()
		self.recipes_list = {'starter': [], 'lunch': [], 'dessert': []}
	
	def get_recipe_by_name(self, name):
		print(1)

	def get_recipe_by_types(self, recipe_type):
		print(2)
		
	def  add_recipe(self, recipe):
		print(3)