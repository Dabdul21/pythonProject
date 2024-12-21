#   Author: Dayan Abdulla
#   Date: 09/10/2024
#   Homework #2 Program #3
#####################################

#user input
def getTemp(num):
    temp = float(input(f"Please enter highest temperature for day {num}: "))
    return temp

#process and Output
def calcTempAverage(temp1, temp2, temp3, count):
    averageTemp = (temp1 + temp2 + temp3) /count
    print(f"The average high temperature over these {count} days was {averageTemp:,.1f}")

#main function
def main():
    count = 0
    temp1 = getTemp(1)
    count += 1
    temp2 = getTemp(2)
    count += 1
    temp3 = getTemp(3)
    count += 1
    calcTempAverage(temp1, temp2, temp3, count)

if __name__ == "__main__":
    main()
