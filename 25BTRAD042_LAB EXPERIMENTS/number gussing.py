import random

def number_guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("=== Number Guessing Game ===")
    print("I have picked a number between 1 and 100. Can you guess it?")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")

            elif guess > secret_number:
                print("Too high! Try again.")

            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break

        except ValueError:
            print("Please enter a valid integer.")


if __name__ == "__main__":
    number_guessing_game()