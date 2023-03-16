import functools
import types

def ft_reduce(func, iter):
	if not isinstance(func, types.FunctionType):
		print("Function parameter is not a function")
		exit()
	if not hasattr(iter, '__iter__'):
		print("Iterable parameter is not iterable")
		exit()
	map_item = iter[0]
	for i in range(1, len(iter)):
		map_item = func(map_item, iter[i])
	return(map_item)
