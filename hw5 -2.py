#Dayan Abdulla
#hw 5 -2
#11/19/2024

BLUE = "\033[1;34m"
RED = "\033[1;31m"
RESET = "\033[0;0m"

# validate the number of years
def validateYears():
    while True:
        try:
            years = int(input("\nHow many years have you been employed at the company? "))
            if years > 0:
                return years
            else:
                print(f"\n{RED}Please enter a number greater than 0.{RESET}")
        except ValueError:
            print(f"\n{RED}Invalid input. Please try again.{RESET}")

#calculate total compensation
def calcCompensation(type, years):
    if type == "1":
        baseSalary = 70000
    elif type == "2":
        baseSalary = 90000
    elif type == "3":
        baseSalary = 120000

    tuitionReimbursement = 4000
    retirement401matching = 0.05
    healthInsurance = 7500

    if years <= 5:
        paidTimeOff = (baseSalary / 52) * 2
    elif years <= 10:
        paidTimeOff = (baseSalary / 52) * 3
    else:
        paidTimeOff = (baseSalary / 52) * 4

    dentalVisionInsurance = 2000
    disabilityLifeInsurance = 5000

    if type == "1":
        compensation = baseSalary + paidTimeOff + tuitionReimbursement + (baseSalary + retirement401matching) + healthInsurance + dentalVisionInsurance + disabilityLifeInsurance
    elif type == "2":
        compensation = baseSalary + paidTimeOff + tuitionReimbursement + (baseSalary + retirement401matching) + healthInsurance + dentalVisionInsurance + disabilityLifeInsurance
    elif type == "3":
        compensation = baseSalary + paidTimeOff + tuitionReimbursement + (baseSalary + retirement401matching) + healthInsurance + dentalVisionInsurance + disabilityLifeInsurance

    return compensation

def main():
    while True:
        print("\n ---- Select Your Position ----\n")
        print("1 - Software Engineer Level I")
        print("2 - Software Engineer Level II")
        print("3 - Manager Level I")
        type = input("\nChoose one of the above (1-3): ")

        while type not in ["1", "2", "3"]:
            type = input(f"\n{RED}Invalid input. Choose one of the above (1-3): {RESET}")

        years = validateYears()
        compensation = calcCompensation(type, years)
        print(f"\n{BLUE}Your total compensation will be ${compensation:,.2f}{RESET}")

        again = input("\nWould you like to calculate another total compensation? (Y/N) ").upper()
        while again not in ["Y", "YES", "N", "NO"]:
            again = input("\nInvalid input. Would you like to calculate another total compensation? (Y/N) ").upper()
        if again in ["N", "NO"]:
            break

if __name__ == "__main__":
    main()

