#   Author: Dayan Abdulla
#   Date: 08/24/2024
#   Homework #1 Program #5
#   Employee Salaries


print("Employee Salaries")
print("------------------------------")

#user input
firstName1 = input("Enter first name: ").capitalize()
salary1 = float(input(f"Enter salary for {firstName1}: "))
firstName2 = input("Enter first name: ").capitalize()
salary2 = float(input(f"Enter salary for {firstName2}: "))
firstName3 = input("Enter first name: ").capitalize()
salary3 = float(input(f"Enter salary for {firstName3}: "))

#output
print(f"\nThe salaries are ${salary1:,.2f}, ${salary2:,.2f}, ${salary3:,.2f}   .")