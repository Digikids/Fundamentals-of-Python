#setup
yes_no = ["yes", "no"]
directions = ["left", "right", "forward", "Backward"]

#introduction
name = input("What is your name, adventurer?\n")
print("Greetings, " + name + ". Let us go on a quest!")
print("You find yourself on the edge of a dark forest.\n")
print("Can you find your way through?\n")

#Start of the game
response = ""
while response not in yes_no:
    response = input("Would you like to step into the forest?\n yes / no \n")
    if response == "yes":
        print("You head into the forest. You hear crows cawwing in the distance.\n")
    elif respose == "no":
        print("You are not ready for this quest. Goodbye, " + name + ".")
        quit()
    else:
        print("I didn't understand that\n")

#Next part
response = ""
while response not in directions:
    print("To your left, you see a bear.\n")
    print("To your right, there is killer bees.\n")
    print("There is a rock wall directly in front of you.")
    print("Behind you is the forest exit.\n")
    response = input("What direction do you move?\nleft/right/forward/backward\n")
    if response == "left":
        print("The bear eats you. Farewell, " + name + ".")
        quit()
    elif response == "right":
        print("You are killed by killer bees. Farewell " +name+".")
    elif response == "forward":
        print("You cannot scale the wall.\n")
        response = "" 
    elif response == "backward":
        print("You leave the forest. Goodbye, " + name + ".")
        quit()
    else:
        print("I didn't understand that.\n")

