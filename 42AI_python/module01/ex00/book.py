from datetime import datetime
from recipe import Recipe

class Book:
	def __init__(self, name, recipes_list):
		if not isinstance(name, str):
			print("Name must be a string")
			exit()
		self.name = name
		self.last_update = datetime.now()
		self.creation_date = datetime.now()
		self.recipes_list = {'starter': [], 'lunch': [], 'dessert': []}
	
	def get_recipe_by_name(self, name):
		if not isinstance(name, str):
			print("Recipe name must be a string")
			exit()
		keys = self.recipes_list.keys()
		for elem in keys:
			for i in range(len(self.recipes_list[elem])):
				if self.recipes_list[elem][i].name == name:
					print(str(self.recipes_list[elem][i]))
					return self.recipes_list[elem][i]
		return (print("No existe esa receta"))

	def get_recipes_by_types(self, recipe_type):
		i = 0
		while i != len(self.recipes_list[recipe_type]):
			print(str(i) + '.- ' + self.recipes_list[recipe_type][i].name)
			i += 1
		
	def  add_recipe(self, recipe):
		if not isinstance(recipe, Recipe):
			print("Recipe must be of class Recipe")
			exit()
		meal_type = recipe.recipe_type
		self.recipes_list[meal_type].append(recipe)
		self.last_update = datetime.now()



# recipe1 = Recipe('salad', 2, 15, ['arugula', 'vinegar', 'lettuce'], 'starter')
# recipe1_1 = Recipe('hummus', 2, 15, ['chickpeas', 'lemonjuice', 'tahini'], 'lunch')
# recipe1_2 = Recipe('asasas', 2, 15, ['chickpeas', 'lemonjuice', 'tahini'], 'lunch')
# recipe2  = Recipe('sandwich', 1, 10, ['ham', 'cheese', 'bread'], 'lunch')
# lst = []
# lst.append(recipe1)
# b1 = Book('recetas', lst)
# b1.add_recipe(recipe2)
# b1.add_recipe(recipe1_1)
# b1.add_recipe(recipe1_2)
# b1.get_recipes_by_types('lunch')
# b1.get_recipe_by_name('hummusj')
