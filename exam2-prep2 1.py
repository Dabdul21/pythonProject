#
#
#
BLUE           = "\033[1;34m"
RED            = "\033[1;31m"
RESET          = "\033[0;0m"

def validateNumber(prompt, min, max):    # validate vin, year, miles
    while True:
        try:
            num = int(input(prompt))
            if num >= min and num <= max:
                return num
            else:
                print(f"\n{RED}Please enter a value between {min} and {max}.{RESET}")
        except ValueError:
            print(f"\n{RED}Invalid value. Please try again.{RESET}")

def addVehicle(vehicles):
    while True:
        flag = 0        # valid VIN
        vin = input("Please enter VIN number: ").upper()
        if len(vin) != 17:
            flag = 1
        if any(char in vin for char in "IQO") :
            flag = 2
        if flag == 0:
            break
        else:
            print(f"{RED}Invalid VIN format.  Must be 17 characters and not contain an I, Q, or O.{RESET}")
    year = validateNumber("Please enter year: ", 1900, 2027)
    make = input("Please enter make: ")
    model = input("Please enter model: ")
    miles = validateNumber("Please enter miles: ", 0, 1000000)
    # add the new vehicle to the list
    vehicles.append([vin, year, make, model, miles])

def displayVehicles(vehicles):
    print(f"\n{'VIN':20} {'Year':10} {'Make':20} {'Model':20} {'Miles':15}")
    print(f"{'----------':20} {'---------':10} {'---------------':20} {'---------------':20} {'------------':15}")
    for x in range(len(vehicles)):  # looping through the rows [rows][columns]  x: 0-4
        print(f'{vehicles[x][0]:<20s} {vehicles[x][1]:<10} {vehicles[x][2]:<20s} {vehicles[x][3]:<20s} {vehicles[x][4]:<15,.0f}')

def main():
    vehicles = []           # create an empty list to store vehicle info (memory)
    # populate the list (VIN, Year, Make, Model, Miles)
    vehicles.append(["888887777766666RR", 2022, "Ford", "Mustang", 11304])    # row 0
    vehicles.append(["666665555577777DD", 2024, "Chevy", "Silverado", 2304])    # row 1
    while True:
        addVehicle(vehicles)
        anotherYN = input("\nWould you like to enter another vehicle (Y/N): ").upper()
        while anotherYN not in ["Y", "YES", "N", "NO"]:     # acceptable responses
            anotherYN = input(f"\n{RED}Invalid response.  Enter Y or N: {RESET}").upper()
        if anotherYN in ["N", "NO"]:
            break                               # break the outer loop
    # formatted outpu
    displayVehicles(vehicles)


if __name__ == "__main__":
    main()