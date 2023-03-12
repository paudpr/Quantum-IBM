import sys
import string

if len(sys.argv) < 3:
	print('Must enter 2 arguments: a string and a integer')
	exit()
try:
	int(sys.argv[2])
except ValueError:
	print("ERROR: Second argument must be an integer")
	exit()
s = sys.argv[1]
n = int(sys.argv[2])

for c in s:
	if c in string.punctuation:
		s = s.replace(c, '')
words_list = [word for word in s.split() if len(word) >  n]
print(words_list)