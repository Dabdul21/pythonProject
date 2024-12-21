BLUE = "\33[1;34m"
RED = "\033[1;31m"
RESET = "\033[0;0m"
BOLD = "\033[1m"


def gameMenu():
    input(f"\n{BLUE}This is the Game Menu stub.{RESET}")

def leaderBoards():
    input(f"\nThis is the LeaderBoards stub.{RESET}")

def options():
    input(f"\nThis is the Options stub.{RESET}")

def minecraftStore():
    input(f"\nThis is the Minecraft Store stub.{RESET}")

def help():
    input(f"\nThis is the Help Store stub.{RESET}")


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

        menuChoice = input(f"\n Enter Menu Choice: ")
        if menuChoice == "L":
            leaderBoards()




if __name__ == "__main__":
    main()