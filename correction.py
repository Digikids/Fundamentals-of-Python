#Question one
nums = [1,2,3,4,5,6,7,8, "Digikids", "Kianda School"]
#a
print("This is the answer of question one a")
print(len(nums))
#b
print("This is the answer of question one b")
for i in nums:
    print(i)

#c
print("This is the answer of question one c")
print(nums[5:9])

#Question Two
print("This is the answer of question two")
def add(a,b):
    print(a + b)

add(3,8)

#Question Three
x = 6
statement = 5 > x

#a
print("This is the answer of question three a")
print(statement)

#b
print("This is the answer of question three a")
if statement:
    print("Five is Greater than x")

#Question four
print("This is the answer of question four")
k = 50
while k <= 100:
    print(k)
    k += 1

#Question five
nums = [1.9,2,3.0,4,5,6.4,7,8, "Digikids", "Kianda School", 8.9]

#a 
print("This is the answer of question five a")
for i in nums:
    if type(i) == int:
        print(i)

#b
print("This is the answer of question five b")
for i in nums:
    if type(i) == str:
        print(i)

#c
print("This is the answer of question five c")
for i in nums:
    if type(i) == float:
        print(i)

#Question six
print("This is the answer of question six")

num1 = int(input("Give me a number: "))
num2 = int(input("Give me a second number: "))

def adds(a, b):
    print(a + b)

def subtract(a, b):
    print(a - b) 

def multiply(a, b):
    print(a * b) 

def divide(a, b):
    print(a / b)

print("What do you want to do with the two numbers?\n1.add\n2.Subtract\n3.Multiply\n4.Divide")
operation = input()

if operation == "1":
    adds(num1, num2)

elif operation == "2":
    subtract(num1, num2)

elif operation == "3":
    multiply(num1, num2)

elif operation == "4":
    divide(num1, num2)

else:
    print("Incorrect input!!!")
    
#Qustion seven
hello = "Hello World"
print(hello)