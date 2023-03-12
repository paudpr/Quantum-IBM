import sys

if len(sys.argv) == 0:
	print("")
	sys.exit(1)
if len(sys.argv) != 3:
	print("Error: input 2 arguments")
	sys.exit(1)
if (sys.argv[1].isdigit() != True) or (sys.argv[2].isdigit() != True):
	print("Error: input must be integers")
	sys.exit(1)	
print("Sum:		" + str(int(sys.argv[1]) + int(sys.argv[2])))
print("Difference: 	" + str(int(sys.argv[1]) - int(sys.argv[2])))
print("Product: 	" + str(int(sys.argv[1]) * int(sys.argv[2])))
if sys.argv[2] == "0":
	print("Quotient: 	" + "ERROR (division by zero)")
	print("Remainder: 	" + "ERROR (modulo by zero)")
else:
	print("Quotient: 	" + str(int(sys.argv[1]) / int(sys.argv[2])))
	print("Remainder: 	" + str(int(sys.argv[1]) % int(sys.argv[2])))
