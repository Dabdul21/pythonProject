#Dayan Abdulla
#09/28/2024
#HW 2 extra credit 2
#############################

def getMpg():
    milesDriven = float(input("Enter how many miles driven: "))
    gallonsUsed = float(input("Enter how many gallons used: "))
    mpg = milesDriven / gallonsUsed  #calc the mpg
    return mpg

def main():
    mpg = getMpg()
    print(f"You got {mpg} mpg on your trip")

if __name__ == "__main__":
    main()