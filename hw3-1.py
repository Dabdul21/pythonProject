#   Author: Dayan Abdulla
#   Date: 09/30/2024
#   Homework #3 Program #1
#####################################

def evalStorm(windSpeed):
    BLUE = "\33[1;34m"
    RESET = "\033[0;0m"

    if windSpeed >= 157:
        print(BLUE + "This is a category 5 hurricane", RESET)
        print(
                "Catastrophic damage will occur: A high percentage of framed homes will be destroyed, with total roof failure and wall collapse. "
                "Fallen trees and power poles will isolate residential areas. Power outages will last for weeks to possibly months. "
                "Most of the area will be uninhabitable for weeks or months."
            )

    elif windSpeed >= 130:
        print(BLUE + "This is a category 4 hurricane", RESET)
        print("Catastrophic damage will occur: Well-built framed homes can sustain severe damage with loss of most of the roof structure and/or some exterior walls. "
              "Most trees will be snapped or uprooted and power poles downed. Fallen trees and power poles will isolate residential areas. Power outages will last weeks to possibly months. "
              "Most of the area will be uninhabitable for weeks or months.")

    elif windSpeed >= 111:
        print(BLUE + "This is a category 3 hurricane", RESET)
        print("Devastating damage will occur: Well-built framed homes may incur major damage or removal of roof decking and gable ends. "
              "Many trees will be snapped or uprooted, blocking numerous roads. Electricity and water will be unavailable for several days to weeks after the storm passes.")

    elif windSpeed >= 96:
        print(BLUE + "This is a category 2 hurricane", RESET)
        print("Extremely dangerous winds will cause extensive damage: Well-constructed frame homes could sustain major roof and siding damage. "
              "Many shallowly rooted trees will be snapped or uprooted and block numerous roads. "
              "Near-total power loss is expected with outages that could last from several days to weeks.")

    elif windSpeed >= 95:
        print(BLUE + "This is a category 1 hurricane", RESET)
        print("Very dangerous winds will produce some damage: Well-constructed frame homes could have damage to roof, shingles, vinyl siding and gutters. "
              "Large branches of trees will snap and shallowly rooted trees may be toppled. "
              "Extensive damage to power lines and poles likely will result in power outages that could last a few to several days.")

    elif windSpeed < 0:
        print(BLUE + "Invalid Speed", RESET)

    elif windSpeed <74:
        print(BLUE + "This is not a hurricane", RESET)

#######################################################################
def main():
    windSpeed = float(input("Please enter sustained wind speed: "))
    evalStorm(windSpeed)

if __name__ == "__main__":
    main()

