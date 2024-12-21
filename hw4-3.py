#   Author: Dayan Abdulla
#   Date: 10/31/2024
#   Homework #4 Program #3
#####################################

BLUE = "\33[1;34m"
RESET = "\033[0;0m"


def userChoices():
    while True:
        print("\n=====MAIN MENU=====")
        painType = input("Enter 'S' if pain is short, sharp and/or shooting \n"
                         "or 'D' if pain is dull, throbbing, and persistent \n"
                         "or 'Q' to Exit:\n").upper()

        if painType == "S":
            while True:
                trigger = input("Enter 'H' if pain triggered by hot or cold drinks or sweets \n"
                                "or 'B' if triggered by biting:\t").upper()

                if trigger == "H":
                    print("\n- Investigate for exposed dentine from gingival recession, a lost filling or caries.")
                    break
                elif trigger == "B":
                    print("\n- Investigate for cracked cusp, loose filling, or fractured tooth.")
                    break
                else:
                    print("\nInvalid choice. Please enter 'H' or 'B'.")

        elif painType == "D":
            while True:
                trigger = input("Enter 'L' if localized, tooth tender to percussion \n"
                                "or 'I' if local inflammation \n"
                                "or 'G' if generalized inflammation and necrosis \n"
                                "or 'D' if local/diffuse pain:\t").upper()

                if trigger == "L":
                    print("\n- Consider possible pulpitis or periapical pathology.")
                    break
                elif trigger == "I":
                    print("\n- Investigate for local inflammation.")
                    break
                elif trigger == "G":
                    print("\n- Consider generalized inflammation and necrosis.")
                    break
                elif trigger == "D":
                    print("\n- Consider possible abscess or localized infection.")
                    break
                else:
                    print("\nInvalid choice. Please enter 'L', 'I', 'G', or 'D'.")

        elif painType == "Q":
            print("Exiting the program.")
            break
        else:
            print("\nInvalid choice. Please enter 'S', 'D', or 'Q'.")
def main():
    userChoices()

if __name__ == "__main__":
    main()