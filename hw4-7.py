#   Author: Dayan Abdulla
#   Date: 10/31/2024
#   Homework #4 Program #7
#####################################

import time
from datetime import datetime

def main():
    while datetime.now().strftime("%p") == "PM":
        currentTime = datetime.now().strftime("%I:%M:%S %p")
        print(f"Time: {currentTime}")
        time.sleep(2)
    print("\nIt's the AM now.")

if __name__ == "__main__":
    main()
