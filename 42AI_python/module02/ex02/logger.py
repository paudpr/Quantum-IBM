import time
import os
from random import randint

def log(func_1):
	def func_2(*args, **kwargs):
		usr = os.environ['USER']
		start = time.time()
		ret_value = func_1(*args, **kwargs)
		end = time.time()
		name = ' '.join(func_1.__name__.split('_'))
		# name_clean = ' '.join(elem for elem in  name)
		try:
			file = open('machine.log', 'x')
		except:
			file = open('machine.log', 'a')
		line =  ''
		line += '(' + usr + ')' + 'Running: ' + name.title() + '\t' + '[ exec_time = ' + f"{(end - start)*1000:2f}" + ' s ]\n'
		file.write(line)
		file.close()
		# return func_1(*args, **kwargs)
		return ret_value
	return func_2

class CoffeeMachine():
	water_level = 100
	@log
	def start_machine(self):
		if self.water_level > 20:
			return True
		else:
			print("Please add water!")
			return False

	@log
	def boil_water(self):
		return "boiling..."

	@log
	def make_coffee(self):
		if self.start_machine():
			for _ in range(20):
				time.sleep(0.1)
				self.water_level -= 1
				print(self.boil_water())
				print("Coffee is ready!")

	@log
	def add_water(self, water_level):
		time.sleep(randint(1, 5))
		self.water_level += water_level
		print("Blu blu blu...")


if __name__ == "__main__":
	machine = CoffeeMachine()
	for i in range(0, 5):
		machine.make_coffee()
	machine.make_coffee()
	machine.add_water(70)

# machine = CoffeeMachine()
# print(os.environ['USER'])
# print(machine.__name__)