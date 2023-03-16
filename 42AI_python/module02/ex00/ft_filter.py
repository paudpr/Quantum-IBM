import types

def ft_filter(func, iter):
	if not isinstance(func, types.FunctionType):
		print("Function parameter is not a function")
		exit()
	if not hasattr(iter, '__iter__'):
		print("Iterable parameter is not iterable")
		exit()
	map_item = []
	for elem in iter:
		if func(elem) == True:
			map_item.append(elem)
	return(map_item)





# def check_even(number):
#     if number % 2 == 0:
#           return True  

#     return False


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # if an element passed to check_even() returns True, select it
# even_numbers_iterator = ft_filter(check_even, numbers)

# # converting to list
# even_numbers = list(even_numbers_iterator)

# print(even_numbers)