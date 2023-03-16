import copy

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
			return False
		scal_product = 0
		for i in range(max(self.shape)):
			product = sum(self.values[i]) * sum(vec.values[i]) 
			scal_product += product
		return scal_product

	def T(self):				
		transpose = list()
		if self.shape[0] == 1:
			for elem in self.values:
				for item in elem:
					transpose.append([item])
		else:
			new_row = list()
			for elem in self.values:
				for item in elem:
					new_row.append(item)
			transpose.append(new_row)
		return Vector(transpose)

	def __add__(self, other):
		if not isinstance(other, Vector):
			print("Both elements must be Vectors for this operation to work")
			return False
		if self.shape != other.shape:
			print("Vectors must have same dimensions")
			return False 
		added = copy.deepcopy(self.values)
		for j in range(len(added)):
			for i in range(len(added[j])):
				added[j][i] += other.values[j][i]
		return added

	def __radd__(self, other):
		return  self + other

	def __sub__(self, other):
		if not isinstance(other, Vector):
			print("Both elements must be Vectors for this operation to work")
			return False
		if self.shape != other.shape:
			print("Vectors must have same dimensions")
			return False 
		added = copy.deepcopy(self.values)
		for j in range(len(added)):
			for i in range(len(added[j])):
				added[j][i] -= other. values[j][i]
		return added

	def __rsub__(self, other):
		return self - other

	def __truediv__(self, other):
		if not isinstance(other, int) and not isinstance(other, float):
			print("NotImplementedError: Vectors can only truediv scalars")
			return False
		if other == 0.0:
			print("Vectors can not truediv by zero")
			return False
		divided = copy.deepcopy(self.values)
		for j in range(len(divided)):
			for i in range(len(divided[j])):
				divided[j][i] /= other
		return divided

	def __rtruediv__(self, other):
		print("NotImplementedError: Division of a scalar by a Vector is not defined here.")
		return False

	def __mul__(self, other):
		if not isinstance(other, int) and not isinstance(other, float):
			print("NotImplementedError: Vectors can only multiplicate scalars")
			return False
		multiplied = copy.deepcopy(self.values)
		for j in range(len(multiplied)):
			for i in range(len(multiplied[j])):
				multiplied[j][i] *= other
		return multiplied

	def __rmul__(self, other):
		return self * other
	
	def __str__(self):
		text = ""
		text += "Vector(" + str(self.values) + ")"
		return text

	def __repr__(self):
		text = ""
		text += "Vector(" + str(self.values) + ")"
		return text