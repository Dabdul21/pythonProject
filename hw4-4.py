#   Author: Dayan Abdulla
#   Date: 10/31/2024
#   Homework #4 Program #4
#####################################

def displayTable(rws, colms, width):
    for r in range(1, rws + 1):
        for c in range(1, colms + 1):
            if r % 2 == 0:
                print(f"Row {r:<5} Columns {c:<{width}}\t\t", end="")
            else:
                print(f"Row {r:<5} Columns {c:<{width}}\t\t", end="")
        print()

def main():
    colms = int(input("Please enter number of columns: \t"))
    rws = int(input("Please enter number of rows:\t"))
    width = int(input("Enter Width: "))
    displayTable(rws, colms, width)

if __name__ == "__main__":
    main()
