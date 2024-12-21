##  Author: Dayan Abdulla
#   Date: 10/30/2024
#   Homework #4 Program #2
#####################################

def main():
    choice = "Y"
    yesList = ("Y", "YES", "y")
    allList = ("Y", "YES", "N", "NO" "y")
    while choice in yesList:
        mph = float(input("\nEnter MPH to convert: "))
        kph = mph * 1.60934
        print(f"{mph} MPH = {kph:,.0f} KPH")
        choice = input("Would you like to make another MPH calculation? (Y/N):") .upper()

        while choice not in allList:
            choice = input("Invalid choice. Enter a Y or N? ").upper()
    print("Goodbye")

if __name__ == "__main__":
    main()