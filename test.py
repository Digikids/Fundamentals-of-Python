def method1(*args):
    for i in args:
        print(i)

method1(90, 45, 56 ,6, 2, 5)

def calculation(a, b):
    print(a * b)
    print(a / b)

calculation(90, 10)

def show_student(student_name, student_age):
    print(f"Their name is {student_name} and they are {student_age} years old")

show_student("Jamie", 12)

n = 50 
while n <= 200:
    print(n)
    n += 1

my_list = []
for i in range(0, 100):
    my_list.append(i)

for j in my_list:
    if j % 4 == 0:
        print(j)

# 1.Write a function method1() such that it can accept 
#     a variable length of  argument and print all arguments value

# 2. Write a function calculation() such that it can accept two 
#     variables and calculate the multiplication and division of them.

# 3. Create a function showStudent() in such a way that it should 
#     accept student name, and their age and display both.

# 4. Print the numbers between 50 and 200 using while loop

# 5. Given a list, iterate it, and display numbers divisible by 4. HINT -> The modulous should be 0 if
# the number is divisible by four.

list = [20, 39, 17, 45, 1, 30, 25, 35, 10, 13, 165]
for i in list:
    if i > 150:
        break
    if i % 5 == 0:
        print(i)


#Question 3
for i in range(4):
    print(i)
else:
    print("done")


#Question 5
i = 1
while i < 4:
    print("*" * i)
    i += 1
i = 5
while i > 0:
    print("*" * i)
    i -= 1


# start = 25
# end = 50
my_list = []
for num in range(1, 100):
    my_list.append(num)

#all the prime greater than 1
#if number is less than or equal to 1, it is not prime
for num in my_list:
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
            else: 
                print(num)


my_list = [20, 39, 17, 13, 45, 1, 13, 30, 25, 35, 10, 13, 13, 165, 20, 39, 17, 13, 45, 1, 13, 30, 25, 35, 10, 13, 13, 165]
for i in my_list:
    count = my_list.count(i)
    print(f"{i} : {count}")

s1 = "Vora"
s2 = "Raahi"
#output = VoRaahira

def appendMiddle(s1, s2):
    middleIndex = int(len(s1) / 2)
    print("original Strings are", s1, s2)
    middleThree = s1[:middleIndex:]+ s2 + s1[middleIndex:]
    print("After appending new string in middle", middleThree)

appendMiddle("Raahi", "Vora")

def evenNums():
    my_list = []
    for i in range(4, 30):
        if i % 2 == 0:
            my_list.append(i)

    print(my_list)

evenNums()

def multiplication_or_sum(num1, num2):
    product = num1 * num2
    #check if priduct is less than 1000
    if product <= 1000:
        print(product)
    else:
        print(num1 + num2)

multiplication_or_sum(4, 7)

for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end = " ")
    print("\t\t")