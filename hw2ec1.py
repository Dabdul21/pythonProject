#Dayan Abdulla
#09/25/2024
#HW 2 extra credit 1
#############################

#func to calculate acres
def calAcres(totalSqFeet):
    sqFeet = 43560
    numAcres = totalSqFeet / sqFeet
    print(f"Number of acres in the tract is: {numAcres:.2f} ")  #displays acres rounded to two decimal places


#handles users input
def main():
    totalSqFeet = float(input("Enter in the total square feet in a tract: "))
    calAcres(totalSqFeet)  #calls user input


if __name__ == "__main__":
    main()
