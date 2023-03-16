import random

def generator(text, sep, opt=None):
	if not isinstance(text, str) or not isinstance(sep, str):
		print('ERROR')
		return False
	strings = text.split(sep)
	if  opt  == 'shuffle':
		for i in range(len(strings) - 1):
			j  = random.randint(0, i + 1)
			strings[i], strings[j] = strings[j], strings[i]
		print(strings)
	elif opt == 'unique':
		strings_set = set(strings)
		strings = (list(strings_set))
		print(strings)
	elif opt == 'ordered':
		strings.sort()
	else:
		print('ERROR')
		return False
	return strings


# lst = generator("esto es es es una prueba una", ' ', 'unique')