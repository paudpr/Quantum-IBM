import sys

if len(sys.argv) < 2:
	print()
	sys.exit(1)
if len(sys.argv) > 2:
	print("AssertionError: more than one argument are provided")
	sys.exit(1)
sys.argv.pop(0)
for item in sys.argv:
	if item.isdigit() == False:
		print("AssertionError: argument is not an integer")
		sys.exit(1)
	else:
		item = int(item)
		if item == 0:
			print("I'm Zero")
		elif item % 2 == 0:
			print("I'm Even")
		elif item % 2 == 1:
			print("I'm Odd")

