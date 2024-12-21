#   Author: Dayan Abdulla
#   Date: 10/3/2024
#   Homework #3 Program #4
#####################################


import re


def checkStrength(password):
    isValid = True

    if len(password) < 10:
        print("Password must be at least 10 characters.")
        isValid = False

    if password.isupper() or password.islower():
        print("Password must be mixed case.")
        isValid = False

    if not any(char.isdigit() for char in password):
        print("Password must contain at least one number.")
        isValid = False

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        print("Password must contain at least one special character.")
        isValid = False

    if isValid == True:
        print("\nPassword is valid")
    else:
        print("\nPassword is invalid")


def main():
    password = input("Please enter a password: ")  # Data type: string
    checkStrength(password)  # Call the function


if __name__ == "__main__":
    main()
