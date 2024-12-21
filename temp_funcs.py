#user input
def getTemp(num):
    temp = float(input(f"Please enter high temperature for day {num}: "))
    return temp

#process and Output
def calcTempAverage(temp1, temp2, temp3, count):
    averageTemp = (temp1 + temp2 + temp3) /count
    print(f"The average height temperature over these {count} days was {averageTemp:,.1f}")

