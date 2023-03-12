import random


num = random.randint(0, 100)
print('This is and interactive guessing game!')
print('You have to enter a number between 1 and 99 to find out the secret nuber.')
print("Type 'exit' to end the game")
print('Good luck!')

def check_type(input):
	try:
		int(guess)
		return True
	except ValueError:
		print("That's not a number")
		return False

print("What's your guess between 1 and 99?")
guess = input('')
count = 1
done = False
while not done:
	if guess  == 'exit':
		print("Goodbye!")
		exit()
	if guess == '42':
		print("The answer to the ultimate question of life, the universe and everything is 42.")
	if not check_type(guess):
		guess = input('')
	if int(guess) > num:
		print("Too high!")
		count += 1
		print("What's your guess between 1 and 99?")
		guess = input('')
	elif int(guess) < num:
		print("Too low!")
		count += 1
		print("What's your guess between 1 and 99?")
		guess = input('')
	elif int(guess) == num:
		print("Congratulations, you got it!")
		print("You won in {c} attempts!" .format(c=count))
		done = True
if count == 1:
	print("Congratulations! You got it on your first try!")
