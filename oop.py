class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def multiply(self):
        return self.a * self.b

    def subtract(self):
        return self.a - self.b

    def divide(self):
        return self.a / self.b


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
obj = Calculator(a, b)


choice = 1

while choice != 0:
    try:
        print("1. Add\n2. Multiply\n3. Subtract\n4. Divide\n0. Exit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            print("Result: ", obj.add())
        elif choice == 2:
            print("Result: ", obj.multiply())
        elif choice == 3:
            print("Result: ", obj.subtract())
        elif choice == 4:
            print("Result: ", obj.divide())
        elif choice == 0:
            print("Exiting the calculator....")
        else:
            print("Invalid choice!!!!")
        
    except ValueError:
        print("Invalid Input!!!")
