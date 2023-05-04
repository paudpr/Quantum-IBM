import numpy as np

class NumPyCreator:

	def __init__(self):
		pass

	def from_list(self, lst, dtype='None'):
		if not isinstance(lst, list):
			return None
		# shape = np.shape(lst[0])
		# for elem in lst:
		# 	if np.shape(elem) != shape:
		# 		print('Creating an ndarray from ragged nested sequences (which is a list-or-tuple of lists-or-tuples-or ndarrays with different lengths or shapes) is deprecated. If you meant to do this, you must specify \'dtype=object\' when creating the ndarray.')
		# 		return None
		arr = np.array(lst, dtype)
		return arr



arr = np.array([[1, 2, 3], [4, 5]])
print(arr)
print(type(arr))

