import sys

if len(sys.argv) == 1:
	print()
elif len(sys.argv) > 1:
	sys.argv.pop(0)
	str = ' '.join(sys.argv)
	str = str[::-1].swapcase()
	print(str)
