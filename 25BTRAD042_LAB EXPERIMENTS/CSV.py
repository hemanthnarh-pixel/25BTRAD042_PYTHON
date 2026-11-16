import csv
import os

filename = "employees.csv"

if not os.path.exists(filename):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "EmployeeID", "Name", "Basic", "Allowance"
        ])

        writer.writerow(["E101", "Rahul", 20000, 3000])
        writer.writerow(["E102", "Priya", 25000, 4000])

total_payroll = 0

try:
    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)

        print("\n--- PAYROLL SUMMARY ---")

        for employee in reader:
            basic = float(employee["Basic"])
            allowance = float(employee["Allowance"])

            gross = basic + allowance
            deduction = gross * 0.10
            net = gross - deduction

            total_payroll += net

            print("\nEmployee ID:", employee["EmployeeID"])
            print("Name:", employee["Name"])
            print("Gross Salary:", round(gross, 2))
            print("Deduction:", round(deduction, 2))
            print("Net Salary:", round(net, 2))

        print("\nTotal Net Payroll:", round(total_payroll, 2))

except (ValueError, KeyError):
    print("Error: Invalid employee data in CSV file.")

except FileNotFoundError:
    print("Employee file not found.")