

BLUE        = "\033[1;34m"
RED         = "\033[1;31m"
RESET       = "\033[0;0m"


def validateBalance():
    # Function to validate the student's balance input
    while True:
        try:
            # Prompt user for balance input
            balance = float(input("Please enter student balance:"))
            # Check if the balance is within the valid range
            if balance >= -10000 and balance <= 10000:
                return balance  # Return valid balance
            else:
                # Prompt user if the balance is out of range
                print("Please enter a balance between -10000 and 10000.")
        except ValueError:
            # Handle invalid (non-numeric) input
            print("Invalid balance. Please try again.")


def addStudents(students):
    # Function to add a student and their balance to the list
    studentName = input("Please enter student name to add:")

    # Ensure a name is entered
    while studentName == "":
        studentName = input("No student name entered. Please enter student name to add:")

    # Ensure the name length does not exceed 50 characters
    while len(studentName) > 50:
        studentName = input("Student name must be 50 or less characters:")

    # Get the validated balance using the validateBalance function
    balance = validateBalance()

    # Append the student name and balance as a list to the students list
    students.append([studentName, balance])


def displayStudents(students):
    # Function to display the list of students and their balances
    print(f"\n{'Student Name':<25} {'Balance':<15}")
    print(f"{'-------------------------':<25} {'---------------':<15}")

    # Iterate through the list of students and display each one
    for x in range(len(students)):
        # Display student name and balance formatted with 2 decimal places
        print(f"{students[x][0]:<25} ${students[x][1]:<15,.2f}")


def displaySummary(students):
    # Function to display a summary of all student balances
    print(f"{'Total students:':<30} {len(students)}")  # Display total number of students

    # Display the smallest and largest balance among all students
    print(f"{'Smallest balance:':<28} {min(row[1] for row in students):,.2f}")
    print(f"{'Largest balance:':<27} {max(row[1] for row in students):,.2f}")


def main():
    # Main function to control the program
    students = []  # Initialize an empty list to store student data

    # Continuously prompt the user to add students
    while True:
        addStudents(students)  # Add a student

        # Ask if the user wants to add another student
        anotherYN = input("\nWould you like to enter another student (Y/N)? ").upper()

        # Validate the response
        while anotherYN not in ("Y", "YES", "N", "NO"):
            anotherYN = input("Invalid response. Please enter Y or N:").upper()

        # Break the loop if the user chooses "N" or "NO"
        if anotherYN in ("N", "NO"):
            break

    # Display the list of students
    displayStudents(students)

    # Display a summary of balances
    displaySummary(students)


# Check if the script is being run directly
if __name__ == "__main__":
    main()  # Run the main function
