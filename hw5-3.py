#Dayan Abdulla
#11/19/24
#hw 5 - 3
def main():
    # Creates and populates a one-dimensional list (in memory/RAM)
    employees = [
        "Jim Bailey",       # 0
        "Amy Dillon",          # 1
        "Ali Nassar",          # 2
        "Jose Martinez",
        "Lenard Phillips",
        "Wally Paulson"
    ]

    # Display the first two elements in the list manually/individually
    print(f"Employee #1: {employees[0]}")
    print(f"Employee #3: {employees[2]}")

    # Display all employees with for loop - method #1
    print("\nAll Employees - For Loop Method #1")
    for employee in employees:
        print(f"Employee: {employee}")

    # # Display all employees with for loop - method #2
    # print("\nAll Employees - For Loop Method #2")
    # for x in range(len(employees)):
    #     print(f"Employee: {employees[x]}")
    #
    # # Display all employees with while loop - method #3
    # print("\nAll Employees - While Loop Method #3")
    # x = 0
    # while x < len(employees):
    #     print(f"Employee #{x + 1}: {employees[x]}")
    #     x = x + 1

    # Add an employee based on user input
    employee = input("\nPlease enter employee name to add to the list: ")
    employees.append(employee)  # Add to end of list

    # Sort the list alphabetically
    employees.sort()

    # Display list again
    print("\nAll Employees - Sorted")
    for employee in employees:
        print(f"Employee: {employee}")

    # Search the list
    employee = input("\nPlease enter employee name to search for: ").title()
    while employee not in employees:
        print("\nEmployee not found.")
        employee = input("\nPlease enter employee name to search for: ").title()
    else:
        print("\nEmployee found.")

    # Display total number of employees
    print(f"\nTotal number of employees: {len(employees)}")


if __name__ == "__main__":
    main()
