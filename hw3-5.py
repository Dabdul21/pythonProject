#   Author: Dayan Abdulla
#   Date: 10/3/2024
#   Homework #3 Program #5
#####################################

BLUE = "\33[1;34m"
RESET = "\033[0;0m"

def main():
    painType = input("Enter 'S' if pain is short, sharp and/or shooting \n or 'D' "
                     "if pain dull, throbbing and persistent: ").upper()
    if painType == "S":
        painTrigger = input("\n Enter 'H' if pain triggered by hot or cold drinks or sweets "
                            "\n or 'B' if triggered by biting: ").upper()

        if painTrigger == "H":
            print(f"{BLUE}\n\tInvestigate for exposed dentine from gingival, a lost filling or caries.{RESET}")
        elif painTrigger == "B":
            print(f"{BLUE}\n\tInvestigate for cracked cusp, loose filling, or a fractured tooth.{RESET}")
        else:
            print("\n\tInvalid choice.")

    elif painType == "D":
        painTrigger = input("\n Enter 'T' if pain is localized and tooth tender to percussion "
                            "\n or 'I' if there is local inflammation "
                            "\n or 'G' if there is generalized inflammation and necrosis "
                            "\n or 'D' if local/diffuse pain: ").upper()

        if painTrigger == "T":
            print("\n\tInvestigate for a periapical infection or sinusitis.")
        elif painTrigger == "I":
            print("\n\tInvestigate for impacted food and pericoronitis.")
        elif painTrigger == "G":
            print("\n\tInvestigate for acute necrotising ulcerative gingivitis.")
        elif painTrigger == "D":
            print("\n\tInvestigate for dry socket or temporomandibular joint disorder.")
        else:
            print("\n\tInvalid choice.")

if __name__ == "__main__":
    main()