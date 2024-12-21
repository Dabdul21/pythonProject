# Exam #1: Functions, Decisions

def healthData():
    steps = int(input("Enter daily steps: "))
    systolic = int(input("Enter systolic value: "))
    diastolic = int(input("Enter diastolic value: "))
    color = input("Your preferred color (b - blue, c - cyan): ")
    return steps, systolic, diastolic, color

def setColor(color):
    if color == "b":
        print("\033[34m")  # Sets text color to blue
    elif color == "c":
        print("\033[36m")  # Sets text color to cyan

def stepAnalysis(steps):
    if steps in range(10000, 20000):
        print("\nFantastic number of steps!")
    elif steps in range(6000, 10000):
        print("\nExcellent good steps. Consult a health care provider to determine if you should walk more.")
    elif steps in range(4000, 6000):
        print("\nVery good steps. You might consider walking more steps. It has many health benefits.")
    else:
        print("\nYou might consider walking more steps. It has many health benefits.")

def bpAnalysis(systolic, diastolic):
    # You will have a formula here
    print(f"\nYour systolic value is {systolic:.2f}")
    print(f"Your diastolic value is {diastolic:.2f}")


def main():
    steps, systolic, diastolic, color = healthData()
    stepAnalysis(steps)
    bpAnalysis(systolic, diastolic)

if __name__ == "__main__":
    main()