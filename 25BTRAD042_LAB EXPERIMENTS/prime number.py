def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


def calculate_factorial(n):
    """Calculate factorial of a non-negative integer using iteration."""
    if n < 0:
        return "Factorial does not exist for negative numbers."

    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


def main():
    print("=== Prime and Factorial Calculator ===")

    try:
        num = int(input("Enter an integer: "))

        # Prime check
        if is_prime(num):
            print(f"{num} is a Prime number.")
        else:
            print(f"{num} is NOT a Prime number.")

        # Factorial check
        fact = calculate_factorial(num)
        print(f"Factorial of {num} is: {fact}")

    except ValueError:
        print("Invalid input. Please enter an integer.")


if __name__ == "__main__":
    main()