#Dayan Abdulla
#09/28/2024
#HW 2 extra credit 3
#############################
def convertC(tempF):
    celsius = (5 / 9) * (tempF - 32)
    print(f"{tempF:.1f} Fahrenheit is equal to {celsius:.2f} Celsius")
    return celsius

def main():
    tempF = float(input("Enter in the temperature in Fahrenheit to convert: "))
    convertC(tempF)

if __name__ == "__main__":
    main()
