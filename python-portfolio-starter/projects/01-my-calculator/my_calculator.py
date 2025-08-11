print("=== Lokesh's CLI Calculator ===")

# Get input from the user
a = float (input("Enter first number:"))
b = float (input("Enter second number:"))
operation = input("choose opertaion (+,-,*,/,%):")

# Perform calculation
if operation == "+":
    print("Result:", a+b)
elif operation == "-":
    print("Result:", a-b)
elif operation == "*":
    print("Result:", a*b)
elif operation == "/":
    if b != 0:
        print("Result:", a/b)
    else:
        print("Error: cannot divide by zero")
elif operation == "%":
    if b!=0:
        print("Result:", a%b)
    else:
        print("Error: cannont modulus by zero")
else:
    print("Invalid operation")