# Simple CLI Calculator

print("Welcome to the Simple Calculator!")
print("Available operations: +, -, *, /")

# Taking user inputs
num1 = float(input("Enter the first number: "))
operation = input("Enter an operation (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

# Perform calculation using if-else
if operation == '+':
    result = num1 + num2
    print("Result:", result)

elif operation == '-':
    result = num1 - num2
    print("Result:", result)

elif operation == '*':
    result = num1 * num2
    print("Result:", result)

elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed.")

else:
    print("Invalid operation selected.")
