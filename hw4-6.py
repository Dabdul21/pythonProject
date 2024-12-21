#   Author: Dayan Abdulla
#   Date: 10/31/2024
#   Homework #4 Program #6
#####################################

import csv, os

def createFile():
    filename = input("Please enter file name to save employee information in: ")
    with open(filename, 'w', newline='') as csvfile:  # create open file
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["First Name", "Last Name", "Title"])
    return filename

def addEmployees(filename):
    firstName, lastName, title = getEmployee()  # call
    with open(filename, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([firstName, lastName, title])  # write
    print(f"\nEmployee information saved in file {filename}")

def getEmployee():
    firstName = input("\nPlease enter employee first name: ").title()
    lastName = input("Please enter employee last name: ").title()
    title = input("Please enter employee title: ").title()
    return firstName, lastName, title

def displayEmployees(filename):
    with open(filename, 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)  # Read the header
        print("{:<20} {:<25} {:<20}".format(*header))  # Print the header row
        for row in csvreader:  # Print data row
            print("{:<20} {:<25} {:<20}".format(*row))


def renameFile(filename):
    newName = input(f"\nEnter new filename to rename file {filename}: ")
    os.rename(filename, newName)
    print("\nFile renamed successfully.")
    filename = newName
    return filename


def deleteFile(filename):
    delYN = input(f"\nConfirm you like to delete file: {filename} (y/n)? ").lower()
    if delYN == "y":
        os.remove(filename)
        print("\nFile deleted.")


def main():
    BLUE = "\033[1;34m"
    RED = "\033[1;31m"
    RESET = "\033[0;0m"

    while True:
        # display menu
        print("\n Employee Menu")
        print("---------------------------")
        print("1. Create employees file")
        print("2. Add employee to file")
        print("3. Display employees file")
        print("4. Rename employees file")
        print("5. Delete employees file")
        print("6. Exit program")

        # get user input
        menuChoice = input("\nPlease enter menu choice (1-6): ")

        if menuChoice == "1":
            filename = createFile()
        elif menuChoice == "2":
            try:
                addEmployees(filename)
            except NameError:
                print(RED + "\nFile not found. Please create a file first." + RESET)
        elif menuChoice == "3":
            try:
                displayEmployees(filename)
            except NameError:
                print(RED + "\nFile not found. Please create a file first." + RESET)
        elif menuChoice == "4":
            try:
                filename = renameFile(filename)
            except NameError:
                print(RED + "\nFile not found. Please create a file first." + RESET)
        elif menuChoice == "5":
            try:
                deleteFile(filename)
                del filename
            except NameError:
                print(RED + "\nFile not found. Please create a file first." + RESET)
        elif menuChoice == "6":
            print(BLUE + "\nGoodbye!" + RESET)
            break
        else:
            print(RED + "\nInvalid choice. Please try again." + RESET)
if __name__ == "__main__":
        main()



