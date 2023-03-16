class Evaluator:
	def __init__(self):
		pass

	def zip_evaluate(coefs, words):
		if not isinstance(coefs, list) or not isinstance(words, list):
			print("Zip_evaluate must recieve list arguments")
			exit()
		if len(words) != len(coefs):
			return(-1)
		sum_elems = 0
		for elem1, elem2 in zip(coefs, words):
			sum_elems += (elem1 * len(elem2))
		return sum_elems

	def enumerate_evaluate(coefs, words):
		if not isinstance(coefs, list) or not isinstance(words, list):
			print("Enumerate_evaluate must recieve list arguments")
			exit()
		if len(words) != len(coefs):
			return(-1)
		sum_elems = 0
		for elem1, elem2 in enumerate(words):
			sum_elems += coefs[elem1] * len(elem2)
		return sum_elems


# words = ["Le", "Lorem", "Ipsum", "est", "simple"]
# coefs = [1.0, 2.0, 1.0, 4.0, 0.5]

# print(Evaluator.zip_evaluate(coefs, words))
# print(Evaluator.enumerate_evaluate(coefs, words))
