#   Author: Dayan Abdulla
#   Date: 09/10/2024
#   Homework #2 Program #4
#####################################

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
    from temp_funcs import *
    main()
