import sys

def text_analyzer(text):
	if isinstance(text, str) == False:
		return (print("AssertionError: argument is not a string"))
	else:
		print("The text contains " + str(len(text)) + " character(s):")
		print(str(sum(1 for c in text if c.isupper())) + " upper letter(s)")
		print(str(sum(1 for c in text if c.islower())) + " lower letter(s)")
		print(str(sum(1 for c in text if c in ".,:;?!")) + " punctuation mark(s)")
		print(str(sum(1 for c in text if c == ' ')) + " space(s)")
	
if len(sys.argv) > 2:
	print("Error: too many arguments")
	sys.exit(1)
elif len(sys.argv) < 2:
	print("Provide a text to analyze")
	text = input()
else:
	text = sys.argv[1]
	text_analyzer(text)