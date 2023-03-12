import sys
import string

MORSE_CODE = { 
	'A':'.-', 
	'B':'-...',	
	'C':'-.-.', 
	'D':'-..', 
	'E':'.',
	'F':'..-.', 
	'G':'--.', 
	'H':'....',
	'I':'..', 
	'J':'.---', 
	'K':'-.-',
	'L':'.-..', 
	'M':'--', 
	'N':'-.',
	'O':'---', 
	'P':'.--.', 
	'Q':'--.-',
	'R':'.-.', 
	'S':'...', 
	'T':'-',
	'U':'..-', 
	'V':'...-', 
	'W':'.--',
	'X':'-..-', 
	'Y':'-.--', 
	'Z':'--..',
	'1':'.----', 
	'2':'..---', 
	'3':'...--',
	'4':'....-', 
	'5':'.....', 
	'6':'-....',
	'7':'--...', 
	'8':'---..', 
	'9':'----.',
	'0':'-----', 
	', ':'--..--', 
	'.':'.-.-.-',
	'?':'..--..', 
	'/':'-..-.', 
	'-':'-....-',
	'(':'-.--.', 
	')':'-.--.-'
	}


def print_morse(morse, lista):
	s = ''
	for phrase in lista:
		for c in phrase:
			if c == ' ':
				s += '/ '
			else:
				s += morse[c.upper()]
				s += ' '
		print(s, end='')

if len(sys.argv) < 2:
	exit()
lista = sys.argv[1::]
for elem in lista:
	for c in string.punctuation:
		if c in elem:
			print("ERROR")
			exit()
print_morse(MORSE_CODE, lista)
