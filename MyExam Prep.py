
def addStudents(students):      #func to add a student and their balance to a list
        studentName = input("Enter your name: ")
#ensures a name is entered
        while studentName == "":
                studentName = input("Enter a correct name to add: ")
#ensure that the len is no more than 50 characters
        while len(studentName) > 50:
                studentName = input("Student name must be 50 or less")

#get validated balance using validateBalace Func
        balance = validateBalance()
        #append student name and balance as a list to the student list
        students.append([studentName, balance])

def validateBalance():
        # Function to validate the student's balance input
        while True:
                try:
                        # Prompt user for balance input
                        balance = float(input("Enter student balance: "))
                        # Check if the balance is within the valid range
                        if balance >=-10000 and balance <= 10000:
                                return balance #return balance
                        else:
                                #prompt use if balance is out of range
                                print("Enter a balance from -10000 to 10000")
                except ValueError:
                        #handle invalid non numeric input
                        print("Invald balance")


def displayStudents(students):
        #func to display a summary of all students and their balances
        print(f"\n{'Student Name':<25} {'Balance':<15}")
        print(f"{'-------------------------':<25} {'---------------':<15}")

#iterate throuh the list os student and display each one
        for x in range(len(students)):
                print(f"{students[x][0]:<25} ${students[x][1]:<15,.2f}")

def displaySummary(students):
        #func to dispay a summary of all student balances
        print(f"{'Total students:':<30} {len(students)}")       #total number of students
        #display smallest and largest balance among all students
        print(f"{'Smallest balance:':<28} {min(row[1] for row in students):,.2f}")
        print(f"{'Largest balance:':<27} {max(row[1] for row in students):,.2f}")
        #total and avaerage added
        print(f"{'Total students:':<30} {len(students)}") #dont even need this already added
        average = sum(row[1] for row in students) / len(students)
        print(f"{'Average balance:':<27} ${average:,.2f}")

def main():
        students = []   #creates an empty list
#prompt use to add students
        while True:
                addStudents(students)   #adds student using the func
                #asks if they wat to add another student
                anotherYN = input("\nWould you like to enter another student (Y/N)? ").upper()

                # Validate the response
                while anotherYN not in ("Y", "YES", "N", "NO"):
                        anotherYN = input("Invalid response. Please enter Y or N:").upper()

                # Break the loop if the user chooses "N" or "NO"
                if anotherYN in ("N", "NO"):
                        break
#display list of students
        displayStudents(students)
        #display a summary of balance
        displaySummary(students)


if __name__ == "__main__":
        main()
