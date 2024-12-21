#Dayan Abdulla
#11/19/24
#hw 5 - 4
def main():
    # Creates an empty list
    employees = []

    # Populate the multi-dimensional list (data in memory)
    employees.append(["55454", "James", "Smith", 67000])
    employees.append(["95433", "Ali", "Bazzi", 99675])
    employees.append(["32366", "Jesus", "Hernandez", 105900])
    employees.append(["56523", "Ralph", "Klein", 54700])
    employees.append(["76789", "Moe", "Hertz", 87400])
    employees.append(["12122", "Jean", "Williams", 98800])

    # Formatted output - required
    print(f"\n{'Employee ID':15} {'First Name':20} {'Last Name':15} {'Salary':15}")
    print(f"{'-------------':15} {'--------------------':20} {'-------------':15} {'-------------':15}")

    # Looping through the rows [rows][columns]
    for x in range(len(employees)):
        print(f"{employees[x][0]:15} {employees[x][1]:20} {employees[x][2]:15} ${employees[x][3]:,.2f}")

    # Display total employees
    print(f"\nTotal employees: {len(employees)}")


if __name__ == "__main__":
    main()