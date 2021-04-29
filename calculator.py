#A program to make a simple calculator.

#This function adds two numbers
def add(x, y):
	return x + y

#This function subtracts two numbers.
def subtract(x, y):
	return x - y

#This function multiplies two numbers.
def multiply(x, y):
	return x * y

#This function divides two numbers.	
def divide(x, y):
	return x / y

def square(x):
    return x * x

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Square")

game_play = True

while game_play  == True:
	#Take input from the user
	choice = input("Enter choice(1/2/3/4): ")

	#Check if choice is one of the four options.
	if choice in ('1', '2', '3', '4', '5'):
		if choice == "5":
			num1 = float(input("Enter a number:"))
			print(num1, "Squared is", square(num1))
		if choice == "1":
			num1 = float(input("Enter first number:"))
			num2 = float(input("Enter the second number:"))
			print(num1, "+", num2, "=", add(num1, num2))
		if choice == "2":
			num1 = float(input("Enter first number:"))
			num2 = float(input("Enter the second number:"))
			print(num1, "-", num2, "=", subtract(num1, num2))

		if choice == "3":
			num1 = float(input("Enter first number:"))
			num2 = float(input("Enter the second number:"))
			print(num1, "*", num2, "=", multiply(num1, num2))

		if choice == "4":
			num1 = float(input("Enter first number:"))
			num2 = float(input("Enter the second number:"))
			print(num1, "/", num2, "=", divide(num1, num2))
			break
	else:
		print("Invalid input!!!")
