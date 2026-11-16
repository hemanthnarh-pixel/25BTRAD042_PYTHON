def simple_calculator():
    print("--- Simple Calculator ---")

    # Get user inputs and convert them to floating-point numbers
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    # Perform arithmetic operations
    print(f"\nAddition: {a + b}")
    print(f"Subtraction: {a - b}")
    print(f"Multiplication: {a * b}")

    # Check for division by zero
    if b != 0:
        print(f"Division: {a / b}")
    else:
        print("Division: Cannot divide by zero")

# Execute the function
simple_calculator()