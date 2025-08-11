def safe_float(s: str):
    try:
        return float(s)
    except ValueError:
        return None

def calculate(a: float, b: float, op: str):
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if op == '/':
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
    raise ValueError("Unsupported operator")

def main():
    print("=== Lokesh's Calculator ===")
    a = safe_float(input("Enter first number: ").strip())
    b = safe_float(input("Enter second number: ").strip())
    op = input("Choose operator (+ - * /): ").strip()

    if a is None or b is None:
        print("Invalid number entered.")
        return
    try:
        result = calculate(a, b, op)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
