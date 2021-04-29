import random #imports the random module
import math

#taking inputs
lower = int(input("Enter Lower bound:- "))

#Taking inputs
upper = int(input("Enter Upper bound:- "))

#Choosing a random number
x = random.randint(lower, upper)
print("\n\t You've only", 
        round(math.log(upper - lower +1, 2)),
        " chances to guess the integer!\n")

# Initializing the number of guesses
count = 0

# guesses depends upon range
while count < math.log(upper - lower + 1, 2):
    count += 1

    #taking in the guess
    guess = int(input("Guess a number:- "))

    #check wheather the guess == x
    if x == guess:
        
        print("Congaltulations you did it in ", count, " guesses")
        break
    elif x > guess:
        print("You guessed too small! ")
    elif x < guess:
        print("You guessed too high!")

#check wheather they are out of gueses
if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is " + str(x))
    print("\tBetter luck next time!!")
    
