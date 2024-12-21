#   Author: Dayan Abdulla
#   Date: 10/3/2024
#   Homework #3 Program #7
#####################################

BLUE = "\33[1;34m"
RED = "\033[1;31m"
RESET = "\033[0;0m"
BOLD = "\033[1m"

def gameMenu():
    input(f"\n{BLUE}This is the Game Menu stub.{RESET}")

def leaderBoards():
    input(f"\n{BLUE}This is the LeaderBoards stub.{RESET}")

def options():
    input(f"\n{BLUE}This is the Options stub.{RESET}")

def minecraftStore():
    input(f"\n{BLUE}This is the Minecraft Store stub.{RESET}")

def help():
    input(f"\n{BLUE}This is the Help Store stub.{RESET}")

def main():
    while True:
        print("\n     Minecraft Menu")
        print("------------------------")
        print("[P]lay Game")
        print("[L]eaderboards")
        print("[O]ptions")
        print("[M]inecraft Store")
        print("[H]elp")
        print("[E]xit")
        menuChoice = input(f"\n{BOLD}Enter menu choice: {RESET}").upper()

        match menuChoice:
            case "P":
                gameMenu()
            case "L":
                leaderBoards()
            case "O":
                options()
            case "M":
                minecraftStore()
            case "H":
                help()
            case "E":
                print(f"{BLUE}\nGoodbye.{RESET}")
                break
            case _:
                print(f"{BLUE}\nInvalid menu choice.{RESET}")




if __name__ == "__main__":
    main()