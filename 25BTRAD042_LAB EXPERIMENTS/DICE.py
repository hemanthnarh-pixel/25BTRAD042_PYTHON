import random

while True:

    print("\n--- DICE SIMULATOR ---")
    print("1. Roll One Die")
    print("2. Roll Two Dice")
    print("3. Roll Multiple Times")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        result = random.randint(1, 6)
        print("Dice result:", result)

    elif choice == "2":
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)

        print("First die:", die1)
        print("Second die:", die2)
        print("Total:", die1 + die2)

    elif choice == "3":
        n = int(input("Enter number of rolls: "))

        if n <= 0:
            print("Enter a positive number.")
            continue

        counts = {i: 0 for i in range(1, 7)}

        for i in range(n):
            result = random.randint(1, 6)
            counts[result] += 1

        print("\n--- FREQUENCY OF RESULTS ---")

        for face, count in counts.items():
            print(face, ":", count)

    elif choice == "4":
        print("Exiting dice simulator.")
        break

    else:
        print("Invalid choice.")