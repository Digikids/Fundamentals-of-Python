#Question1
def method1(*args):
    for i in args:
        print(i)

method1(3)

def calculation(a, b):
    addation = a * b
    subtraction = a / b
    print(f"The product is {addation}\nThe divsion is {subtraction}")

calculation(8, 6)

def showStudent(student_name, student_age):
    print(f"Their name is {student_name} and they are {student_age} years old")

showStudent("Raahi", 12)

i = 50
while i <= 200:
    print(i)
    i += 1

my_list = []
for i in range(200):
    my_list.append(i)
for j in my_list:
    if j % 4 == 0:
        print(j)