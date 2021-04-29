#Import the random module
import random

#initialize player scores to 0
player1_score = 0
player2_score = 0

valid_numbers = [1, 2, 3, 4, 5, 6]
#Repeat everything in this block 10 times
for i in range(10):

    #Generate random numbers
    try:
        player1_value =  int(input("Give me a random number between 1 and 6: "))
        player2_value = random.randint(1,6)
        if player1_value in valid_numbers:
            #display the values
            print("You rolled: ", player1_value)
            print("Computer rolled: ", player2_value)

            #introduce the gameplay
            int(player1_value)
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
        else:
            print("Invalid input!!!!")

    except ValueError:
        print("Invalid input!!!")
    
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