print("=== Lokesh's CLI Calculator ===")

# Get input from the user
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Choose operation (+, -, *, /): ")

# Perform calculation
if operation == "+":
    print("Result:", a + b)
elif operation == "-":
    print("Result:", a - b)
elif operation == "*":
    print("Result:", a * b)
elif operation == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error: Cannot divide by zero")
else:
    print("Invalid operation")
