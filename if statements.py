
number_1 = int(input("Input a number: "))
number_2 = int(input("Input a second number: "))

operation = input("What do you want to do with the two numbers: ")
output = ""

if operation == "+":
    output = number_1 + number_2
elif operation == "-":
    output = number_1 - number_2
elif operation == "*":
    output = number_1 * number_2
elif operation == "/":
    output = number_1 / number_2
else:
    print("Ivalid selection!!!!!!")

print("The answer is: " + str(output))
