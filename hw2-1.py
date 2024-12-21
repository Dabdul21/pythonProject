#   Author: Dayan Abdulla
#   Date: 09/10/2024
#   Homework #2 Program #1
#####################################



def main ():
    import time
    curr24Time = time.strftime("%H:%M:%S", time.localtime())

    curr12Time = time.strftime("%I:%M:%S %p", time.localtime())

    print("Current standard time is:", curr12Time)

    print("Current 24 time is:", curr24Time)

if __name__ == "__main__":
        main()      #Calling main function
