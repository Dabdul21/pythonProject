#   Author: Dayan Abdulla
#   Date: 10/3/2024
#   Homework #3 Program #2
#####################################

def userMenu():
    print("1 - In District")
    print("2 - Out of District Student")
    print("3 - Out of State / International Student")

    type = input("\nChoose one of the above (1-3): ")
    while type not in ("1", "2", "3"):
        type = input("\nInvalid input. Please enter choice (1-3): ")
    return type

def calTution(type, credits1, credits2):
    if type == "1":
        tuition = (credits1 *105.75) + (credits2 * 200) + ((credits1 + credits2) * 23) + 50 + 60

    elif type == "2":
        tuition = (credits1 *202) + (credits2 * 265) + ((credits1 + credits2) * 24) + 50 + 60

    elif type == "3":
        tuition = (credits1 *295.50) + (credits2 * 350) + ((credits1 + credits2) * 24) + 50 + 60


    return tuition


def main():
    type = userMenu()
    credits1 = float(input("How many 100-200 level credits do you plan to register for? "))
    credits2 = float(input("How many 300-400 level credits do you plan to register for? "))
    #optional so it does not
    while (credits1 <= 0 and credits2 <= 0):
        print("\nInvalid credit hours. Please enter at least 1.")

    tuition = calTution(type, credits1, credits2)
    print(f"You owe {tuition}")

if __name__ == "__main__":
   main()
