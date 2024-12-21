#Dayan Abdulla
#11/10/24
#hw 5-1

BLUE = "\033[1;34m"
RED = "\033[1;31m"
RESET = "\033[0;0m"


def getAge():
    while True:
        try:
            age = float(input("Enter a number: "))
            if age in range (16,131):
                return age
            else:
                print(f"\n{RED} Age MUST be in between 16 and 130. {RESET}")
        except:
            print(f"{RED} \nInvalid age. {RESET}")

def main():
    employeeAges = []
    while True:
        age = getAge()
        employeeAges += [age]
        anotherYN = input("\nWould you like to enter another age (Y/N)? ").upper()
        while anotherYN not in ("Y", "y", "Yes", "N", "n", "No"):
            anotherYN = input(f"{RED}\nResponse Invalid! Enter a Y or N ")

        if anotherYN in ("N", "No", "n"):
            print("\nGoodbye program ended ")
            break



if __name__ == "__main__":
    main()