#Guess the number
import random

solution=random.randint(0,1000)
print "Guess the number game: \n"

guess=int(raw_input("Enter your guess: "))

while solution!=guess:
	if guess<solution:
		print "Solution is greater than "+str(guess)+"\n"
	else:
		print "Solution is lesser than "+str(guess)+"\n"
	guess=int(raw_input("Enter your guess: "))

print "Congratulations"


