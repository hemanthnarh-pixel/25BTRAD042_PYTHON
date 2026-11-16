import json
import os

filename = "students.json"

if os.path.exists(filename):
    with open(filename, "r") as file:
        try:
            students = json.load(file)
        except json.JSONDecodeError:
            students = []
else:
    students = []

while True:
    print("\n--- STUDENT DATA MANAGER ---")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Display Students")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        roll = input("Enter roll number: ")

        if any(s["roll"] == roll for s in students):
            print("Roll number already exists.")
            continue

        name = input("Enter student name: ")
        marks = float(input("Enter marks: "))

        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100.")
            continue

        students.append({
            "roll": roll,
            "name": name,
            "marks": marks
        })

        with open(filename, "w") as file:
            json.dump(students, file, indent=4)

        print("Student added successfully.")

    elif choice == "2":
        roll = input("Enter roll number to search: ")
        found = False

        for student in students:
            if student["roll"] == roll:
                print(student)
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "3":
        roll = input("Enter roll number to update: ")
        found = False

        for student in students:
            if student["roll"] == roll:
                name = input("Enter new name: ")
                marks = float(input("Enter new marks: "))

                if not 0 <= marks <= 100:
                    print("Invalid marks.")
                    found = True
                    break

                student["name"] = name
                student["marks"] = marks
                found = True

                print("Student updated successfully.")
                break

        if found:
            with open(filename, "w") as file:
                json.dump(students, file, indent=4)
        else:
            print("Student not found.")

    elif choice == "4":
        if not students:
            print("No student records available.")
        else:
            for student in students:
                print("Roll:", student["roll"],
                      "Name:", student["name"],
                      "Marks:", student["marks"])

    elif choice == "5":
        print("Exiting Student Data Manager.")
        break

    else:
        print("Invalid choice.")