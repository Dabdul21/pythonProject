#
#
#
def main():
    score = float(input("Please enter exam score: "))

    if score in range(90, 101):
        print("You got an A.")
    elif score in range(80, 90):
        print("You got an B.")
    elif score in range(70, 80):
        print("You got an C.")
    elif score in range(60, 70):
        print("You got an D.")
    elif score in range(0, 60):
        print("You got an E.")
    else:
        print("Invalid score")

if __name__ == "__main__":
    main()
