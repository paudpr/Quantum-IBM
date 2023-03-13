class Vector:
	def __init__(values, shape):
		if not isinstance(values, lst):
			print("Vector values must be a list")
			exit()
		for elem in values:
			if not isinstance(elem, lst):
				print("Vector values must contain lists")
				exit()
		self.values = values
		if not isinstance(shape, tuple):
			print("Shape must be a tuple")
			exit()
		if (shape[0] or shape[1]) != 1:
			print("One of the dimensions must be 1 for it to be a vector")
			exit()
		self.shape = shape

	def dot():
		