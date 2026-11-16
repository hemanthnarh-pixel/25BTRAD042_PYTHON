def fibonacci_recursive(n):
    """Return the nth Fibonacci number (0-indexed)."""

    if n <= 0:
        return 0

    elif n == 1:
        return 1

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def main():
    print("=== Fibonacci Series Using Recursion ===")

    try:
        terms = int(input("Enter the number of terms to display: "))

        if terms <= 0:
            print("Please enter a positive integer.")

        else:
            print(f"Fibonacci series ({terms} terms):")

            series = [str(fibonacci_recursive(i)) for i in range(terms)]

            print(", ".join(series))

    except ValueError:
        print("Invalid input. Please enter an integer.")


if __name__ == "__main__":
    main()