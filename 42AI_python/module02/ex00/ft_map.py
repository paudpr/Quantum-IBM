import types

def ft_map(func, iter):
	if not isinstance(func, types.FunctionType):
		print("Function parameter is not a function")
		exit()
	if not hasattr(iter, '__iter__'):
		print("Iterable parameter is not iterable")
		exit()	
	map_item = []
	for elem in iter:
		map_item.append(func(elem))
	return(map_item)




# def addition(n):
#     return n + n

# # # We double all numbers using map()
# numbers = (1, 2, 3, 4)
# a = {"a": 21, "b": 1}
# result = ft_map(addition, a)
# print(list(result))
# print(tuple(result))


# prueba = map(addition, tuple(numbers))
# print(prueba)
# print(type(prueba))