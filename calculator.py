# calculator.py

# Functions for operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

# Main program loop
def calculator():
    print("=== Simple Calculator CLI ===")
    print("Operations: +, -, *, /")
    print("Type 'exit' to quit.\n")

    while True:
        # Take operator input
        operator = input("Enter operation (+, -, *, /) or 'exit': ").strip()

        if operator.lower() == "exit":
            print("Exiting calculator. Goodbye!")
            break

        if operator not in ["+", "-", "*", "/"]:
            print("Invalid operation! Please try again.\n")
            continue

        try:
            # Take number inputs
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            # Perform calculation
            if operator == "+":
                result = add(num1, num2)
            elif operator == "-":
                result = subtract(num1, num2)
            elif operator == "*":
                result = multiply(num1, num2)
            elif operator == "/":
                result = divide(num1, num2)

            print(f"Result: {result}\n")

        except ValueError:
            print("Invalid input! Please enter numeric values.\n")

# Run calculator
if __name__ == "__main__":
    calculator()
