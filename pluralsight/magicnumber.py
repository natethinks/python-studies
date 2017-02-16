import random

print("What is your favorite number?")
number = input()

print("Your favorite number is " + str(number))

magicNumber = random.randint(1, 100)

print("I'm thinking of a number between 1 and 100")

found = False

while not found:
	guess = input()
	if (guess > magicNumber):
		print ("Too high")
	if (guess < magicNumber):
		print ("Too low")
	if (guess == magicNumber):
		found = True
print ("You got it!")

