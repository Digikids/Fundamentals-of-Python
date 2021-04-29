#Import the random module
import random

#initialize player scores to 0
player1_score = 0
player2_score = 0

#Repeat everything in this block 10 times
for i in range(10):

    #Generate random numbers
    player1_value = int(input("Give me a random number between 1 and 6: "))

    while player1_value <= 0 or player1_value > 6:
        player1_value = int(input("The number must be between 1 and 6, including both and 1 and 6: "))

    print(type(player1_value))
    # if users were playing the game 
    #use player1_value = input("Give me a random number between 1 and 6")
    player2_value = random.randint(1,6)

    #display the values
    print("you rolled: ", player1_value)
    print("computer rolled: ", player2_value)

    #introduce the gameplay
    if player1_value > player2_value:
        print("Player 1 won!!")
        player1_score += 3
    elif player2_value > player1_value:
        print("Player 2 won!!")
        player2_score += 3
    else:
        print("It's a draw")
        player2_score += 1
        player1_score += 1
    
    input("Press enter to continue.")


print("### Game Over ####")
if player1_score > player2_score:
    print("Player 1 won")
    print("Player 1 score: ", player1_score)
    print("Player 2 score: ", player2_score)
elif player1_score < player2_score:
    print("Player 2 won")
    print("Player 1 score: ", player1_score)
    print("Player 2 score: ", player2_score)
else:
    print("It is a draw")
    print("Player 1 score: ", player1_score)
    print("Player 2 score: ", player2_score)