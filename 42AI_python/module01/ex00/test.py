from Recipe import recipe
from Book import book

print("Test 1 - Recipe")
print('--> check if every instance is as it should, by type')

def test_1():
	r1 = Recipe('salad', 2, 15, ['arugula', 'vinegar', 'lettuce'], 'starter')
	# paso, pereza
