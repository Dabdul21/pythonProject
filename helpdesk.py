#   Author: Dayan Abdulla
#   Date: 10/31/2024
#   Homework #4 Program #5 helpdesk
#####################################

# helpdesk.py

import diagnose  # Import

def mainMenu():
    while True:
        print("\n     METROPOLITIAN MEDICAL CENTER")
        print("         IT Services HelpDesk")
        print("------------------------------")
        print("1. Diagnostic Utility")
        print("2. Submit Trouble Ticket")
        print("3. Exit Program")

        diagChoice = input("What would you like to do? (1-3): ")

        if diagChoice == "1":
            diagnose.diagnosticMenu()  # Call the diagnostic menu from diagnose.py
        elif diagChoice == "2":
            input("\nSubmit Trouble Ticket.\nThis is a stub. Press [Enter] to continue.")
        elif diagChoice == "3":
            print("Goodbye!")
            break  # Exit the program
        else:
            print("\nInvalid menu choice. Please enter a menu choice of 1-3.")


if __name__ == "__main__":
    mainMenu()


