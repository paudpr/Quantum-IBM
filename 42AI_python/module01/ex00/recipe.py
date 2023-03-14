class Recipe:
	def __init__(self, name, cooking_lvl, cooking_time, ingredients, recipe_type, description = str()):
		if not isinstance(name, str):
			print("Name must be a string")
			exit()
		self.name = name
		if not isinstance(cooking_lvl, int) or 1 > cooking_lvl > 5:
			print("Cooking level must be a int between 1 and 5")
			exit()
		self.cooking_lvl = cooking_lvl
		if not isinstance(cooking_time, int) or cooking_time < 0:
			print("Cooking time must be a positive integer")
			exit()
		self.cooking_time = cooking_time
		if not isinstance(ingredients, list):
			print("Ingredients must be a list")
			exit()
		for elem in ingredients:
			if not isinstance(elem, str):
				print("Each ingredint must be a string")
				exit()
		self.ingredients = ingredients
		if not isinstance(recipe_type, str) or recipe_type not in ['starter', 'lunch', 'dessert']:
			print("Recipe type must be: 'starter', 'lunch' or 'dessert'")
			exit()
		self.recipe_type = recipe_type
		if not isinstance(description, str):
			print("Descriptiom must be a string")
			exit()
		self.description = description
	def __str__(self):
		text = ""
		text += self.name.upper() + ' -> '
		text += '[lvl: ' + str(self.cooking_lvl) + '] '
		text += '[time: ' + str(self.cooking_time) + 'min] '
		text += '[ingredients: ' 
		for ing in self.ingredients:
			text += ing + ', '
		text += '] '
		text += '[type: ' + self.recipe_type + '] '
		text += '[description: ' + self.description + ']'
		return text

# recipe1  = Recipe('salad', 2, 15, ['arugula', 'vinegar', 'lettuce'], 'starter')
# print(str(recipe1))
