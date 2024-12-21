BLUE            = "\033[1;34m"
RED             = "\033[1;31m"
RESET          = "\033[0;0m"


# prints welcome statement
print(f"{BLUE}Welcome to Checkout{RESET}")

# allows user to input prices for products
def getPrice():
    while True:
        try:
            price = float(input("\nPlease enter price of item: $"))
            if price < 1:
                print(f"\n{RED}Invalid price. Price must be greater than $0. Please try again.{RESET}")
                price = getPrice()
        except ValueError:
            print(f"\n{RED}Invalid price. Please enter a price{RESET}")
        else:
            print(f"\n{BLUE}${price:.2f} has been added to the total{RESET}")
            break
    return price

# main program
# creates one dimensional list
def main():
    response = "Y"
    priceList = []
    while response.upper() in ("YES", "Y"):
        add = getPrice()
        priceList += [add]

# user input and input validation for if user would like to add more product prices
        response = input("\nWould like to enter another item (Y/N)? ")
        while response.upper() not in ("YES", "Y", "NO", "N"):
            response = input(f"\n{RED}Invalid choice. Please enter Y or N? {RESET}")

# prints output
    print(f"{BLUE}{'Total number of items: ' :<30s} {len(priceList):.2f}{RESET}")   # total amount of numbers entered
    print(f"{BLUE}{'Least expensive item price: '          :<30s} ${min(priceList):.2f}{RESET}") # smallest number or minimum number entered
    print(f"{BLUE}{'Most expensive item price: '          :<30s} ${max(priceList):.2f}{RESET}") # biggest or maximum number in the list
    print(f"{BLUE}{'Total bill is:':<30s} ${sum(priceList)}{RESET}")

# tells the program to run
if __name__ == "__main__":
    main()
