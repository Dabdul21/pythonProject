#Dayan Abdulla
#11/19/24
#hw 5 - 5

# Define color constants
BLUE = "\033[1;34m"
RED = "\033[1;31m"
RESET = "\033[0m"

# Validate salary input
def validateSalary():
    while True:
        try:
            salary = float(input("Please enter employee salary: "))
            if salary > 0:
                return salary
            else:
                print(f"\n{RED}Please enter a salary greater than 0.{RESET}")
        except ValueError:
            print(f"\n{RED}Invalid input. Please try again.{RESET}")

# Display employees
def displayEmployees(employees):
    print(f"{BLUE}{'Employee Name':25} {'Salary':15}{RESET}")
    print(f"{'---------------------':25} {'---------------':15}")
    for x in range(len(employees)):  # Looping through the rows
        print(f"{employees[x][0]:<25} ${employees[x][1]:<15,.2f}")  # Multi-dimensional list
    # Output summary
    print(f"\n{BLUE}Total employees: {'':20} {len(employees)}{RESET}")
    salaries = [employee[1] for employee in employees]
    averageSalary = sum(salaries) / len(salaries)
    print(f"{BLUE}Average salary: {'':20} ${averageSalary:<15,.2f}{RESET}")

# Search for an employee
def searchEmployee(employees):
    employeeName = input("\nPlease enter employee name to search for: ")
    flag = 0  # Employee not found
    for x in range(len(employees)):  # Looping through rows
        if employees[x][0] == employeeName:
            print(f"{BLUE}\nEmployee found. Salary: ${employees[x][1]:<15,.2f}{RESET}")
            flag = 1  # Employee found
    if flag == 0:
        print(f"{BLUE}\nEmployee not found.{RESET}")

# Display main menu
def mainMenu():
    print(f"\n{BLUE}Dearborn Computers{RESET}")
    print("------------------------")
    print("1. Display All Employees")  # Run function
    print("2. Add an Employee")        # Run function
    print("3. Search Employees")       # Run function
    print("4. Exit")                   # Ends the loop
    menuChoice = input(f"\n{BLUE}Enter menu choice: {RESET}")  # String
    return menuChoice

# Add an employee
def addEmployee(employees):
    employeeName = input("\nPlease enter employee name to add: ")  # Get user input
    while employeeName == "":
        employeeName = input(f"\n{RED}Invalid employee name. Please enter employee name to add:{RESET} ")
    employeeSalary = validateSalary()  # Get user input and validate it
    employees.append([employeeName, employeeSalary])  # Add a row/employee to the list

# Main function
def main():
    # Create and populate a list (store in memory/RAM)
    employees = [["Robert Smith", 48000.50], ["Mohammed Bazzi", 89500], ["Sarah Walls", 79800]]

    while True:
        menuChoice = mainMenu()  # Display menu and get user input
        if menuChoice == "1":
            displayEmployees(employees)  # Run the appropriate function
        elif menuChoice == "2":
            addEmployee(employees)
        elif menuChoice == "3":
            searchEmployee(employees)
        elif menuChoice == "4":  # Exiting the program
            print(f"\n{BLUE}Goodbye{RESET}")
            break  # Break the while loop
        else:
            print(f"\n{RED}Invalid menu choice.{RESET}")

if __name__ == "__main__":
    main()
