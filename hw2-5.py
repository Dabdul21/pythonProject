#   Author: Dayan Abdulla
#   Date: 09/10/2024
#   Homework #2 Program #5
#####################################


def calChange(change):
    quarters = change // 25
    change = change % 25
    dimes = change // 10
    change = change % 10
    nickels = change // 5
    change = change % 5
    pennies = change // 1

#rEsults
    print(f"Number of quarters: {quarters}")
    print(f"Number of dimes: {dimes}")
    print(f"Number of nickels: {nickels}")
    print(f"Number of pennies: {pennies}")


def main():
    change = int(input("Please enter amount the amount of cents "))
    calChange(change)


if __name__ == "__main__":
    main()