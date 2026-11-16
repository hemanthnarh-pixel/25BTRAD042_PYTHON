students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = float(input("Enter marks out of 100: "))

    students[name] = marks

print("\n--- STUDENT RESULTS ---")

for name, marks in students.items():

    if marks >= 90:
        grade = "A+"

    elif marks >= 75:
        grade = "A"

    elif marks >= 60:
        grade = "B"

    elif marks >= 35:
        grade = "C"

    else:
        grade = "Fail"

    print("Name:", name)
    print("Marks:", marks)
    print("Grade:", grade)
    print("-------------------")