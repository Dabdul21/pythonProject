#   Author: Dayan Abdulla
#   Date: 10/31/2024
#   Homework #4 Program #1
#####################################
BLUE = "\33[1;34m"
RESET = "\033[0;0m"

def main():
    runningTotal = 0
    max = int(input("Please enter a maximum number: "))

    print("\nDivisible by 3\t\tRunning Total")

    for x in range (3, max + 1, 3):             #taking in start, stop and step by using range
        runningTotal = runningTotal + x
        if x % 2 == 0:                      #checks if x is even
            print(f"{BLUE}{x:<20,} {runningTotal:}{RESET}")
        else:
            print(f"{x:<20,} {runningTotal:}")

if __name__ == "__main__":
    main()