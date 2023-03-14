class Vector:
	def __init__(self, values):
		if not isinstance(values, list):
			print("Vector values must be a list")
			exit()
		for elem in values:
			if not isinstance(elem, list):
				print("Vector values must contain lists")
				exit()
			for thing in elem:
				if not isinstance(thing, float):
					if isinstance(thing, int):
						thing = float(thing)
					else:
						print("Vector values contains non-float values")
						exit()
		self.values = values
		x, y = len(self.values), len(self.values[0])
		self.shape = tuple((x, y))

	def dot(self, vec):
		if self.shape != vec.shape:
			print("Shapes mmust be equal for scalar product")
			exit()
		scal_product = 0
		for i in range(max(self.shape)):
			product = sum(self.values[i]) * sum(vec.values[i]) 
			scal_product += product

	# no está bien
	# def T(self):				
	# 	self.shape = tuple((self.shape[1], self.shape[0]))

	def __add__(self, other):
		if self.shape != other.shape:
			print("Vectors must have same dimensions")
			exit()
		# i = 0
		added = []
		for a, b in zip(self.values, other.values):
			added.append([a + b])
		print(added)
		print(range(len(added)))
		for i in range(len(added)):
			added[i] = sum(added[i])
		print(added)
		return added
