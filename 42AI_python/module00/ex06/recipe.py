cookbook = {
	'sandwich': {
		'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
		'meal': 'lunch',
		'prep_time': 10
	},
	'cake': {
		'ingredients': ['flour', 'sugar', 'eggs'],
		'meal': 'dessert',
		'prep_time': 60
	},
	'salad': {
		'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
		'meal': 'lunch',
		'prep_time': 15
	}
}

def print_list(lista):
	for i in range(len(lista) - 1):
		print(lista[i] + ', ', end='')
	print(lista[i + 1] + '.')

def list_recipe(cookbook):
	for elem in cookbook:
		print(elem)

def list_details(recipe):
	print('This are the recipe details:')
	keys = recipe.keys()
	for key in recipe.keys():
		if key == 'ingredients':
			print('ingredients: ', end='')
			print_list(recipe[key])
		else:
			print('{key}: {values}'  .format(key=key, values=recipe[key]))

def del_recipe(cookbook, recipe):
	if recipe in cookbook.keys():
		del cookbook[recipe]
		print("Recipe deleted")
	else:
		print("This recipe does not exist")

def add_recipe(cookbook):
	print("Enter a name: ")
	recipe = input("")
	cookbook.update({recipe: {}})
	print("Enter ingredients: ")
	done = False
	ingredients = []
	while (not done):
		ing = input("")
		if ing == "":
			done = True
		else:
			ingredients.append(ing)
	cookbook[recipe].update({'ingredients': ingredients})
	print("Enter meal type: ")
	meal = input('')
	cookbook[recipe].update({'meal': meal})
	print("Enter preparation time: ")
	time = input('')
	cookbook[recipe].update({'prep_time': int(time)})

def print_options():
	print("List of the available options:")
	print("1: Add a recipe")
	print("2: Delete a recipe")
	print("3: Print a recipe")
	print("4: Print the cookbook")
	print("5: Quit")
	print('')	

print("Welcome to the Python Cookbook !")
print_options()
print("Please select an option")
opt = input('')
done = False
while (not done):
	if opt.isdigit() == False:
		print("Sorry, this option does not exist.")
		print_options()
	elif int(opt) == 1:
		add_recipe(cookbook)
	elif int(opt) == 2:
		print("Please enter a recipe name to delete")
		recipe = input('')
		del_recipe(cookbook, recipe)
	elif int(opt) == 3:
		print("Please enter a recipe name to get its details")
		recipe = input('')
		list_details(cookbook[recipe])
	elif int(opt) == 4:
		for elem in cookbook.keys():
			print(elem)
			list_details(cookbook[elem])
			print('')
	elif int(opt) == 5:
		print("Cookbook closed. Goodbye!")
		exit()
	else:
		print("Sorry, this option does not exist.")
		print_options()
	
	print("\nPlease select an option")
	opt = input('')