# defining operations
def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def division(num1, num2):
    return num1 / num2


def multiply(num1, num2):
    return num1 * num2


operation = input("Choose an operation:")

num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))

if operation == "add":
    print(num1 + num2)

elif operation == "subtract":
    print(num1 - num2)

elif operation == "multiply":
    print(num1 * num2)

elif operation == "divide":
    print(num1 / num2)

else:
    print("Operation not available")


