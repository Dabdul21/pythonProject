#   Author: Dayan Abdulla
#   Date: 09/25/2024
#   Homework #2 Program #7
#####################################

import csv          #just the import csv library

#gather employee information
def employeeInfo():
    firstName = input("Please enter employee first name: ").title()
    lastName = input("Please enter employee last name: ").title()
    title = input("Please enter employee title: ").title()
    return firstName, lastName, title


def main():
    fileName = input("Please enter file name to save employee information in (.csv) ")
    # blank line for readability
    print("\n")

    #Open file in writer mode
    with open(fileName, 'w',) as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(["First Name", "Last Name", "Title"])    #writes the header

            #1 employee
            firstName, lastName, title = employeeInfo()
            csvwriter.writerow([firstName, lastName, title])

            #blank line for readability
            print("\n")

            #2 employee
            firstName, lastName, title = employeeInfo()
            csvwriter.writerow([firstName, lastName, title])

    #prints where info saved
    print(f"Employee information saved in file {fileName}")
if __name__ == "__main__":
        main()
