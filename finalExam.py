

print(f"{'Kroger Checkout':<25} ")
print(f"{'-------------------------':^25} ")

def validateBalance():
    # Function to validate the items's balance input
    while True:
        try:
            # Prompt user for balance input
            balance = float(input("Please enter price: $ "))
            # Check if the balance is within the valid range
            if balance >= 0 :
                return balance  # Return valid balance
            else:
                # Prompt user if the balance is out of range
                print("Please enter a price more than 0 .")
        except ValueError:
            # Handle invalid (non-numeric) input
            print("Invalid price. Please try again.")


def getOrder(list):
    # Function to add a item and their price to the list
    itemName = input("Please enter item name: ")

    # Ensure a name is entered
    while itemName == "":
        itemName = input(f"\n No item name entered. Please enter item name to add:")

    # Get the validated balance using the validateBalance function
    balance = validateBalance()

    # Append the item name and balance as a list to the item list
    list.append([itemName, balance])


def displayItems(list):
    # Function to display the list of Items and their price
    print(f"\n{'Item Name':<30} {'Item Price':<15}")
    print(f"{'-----------':<30} {'-----------':<15}")

    # Iterate through the list of items and display each one
    for x in range(len(list)):
        # Display item name and balance formatted with 2 decimal places
        print(f"{list[x][0]:<30} ${list[x][1]:<15,.2f}")


def displaySummary(list):
    # Function to display a summary of all items and  balances
    print(f"{'Total items ordered:':<30} {len(list)}")  # Display total number of items

    # Display the smallest and largest balance among all items
    print(f"{'Least expensive item:':<30} ${min(row[1] for row in list):,.2f}")
    print(f"{'Most expensive item:':<30} ${max(row[1] for row in list):,.2f}")


def main():
    # Main function to control the program
    list = []  # Initialize an empty list to store item data

    # Continuously prompt the user to add items
    while True:
        getOrder(list)  # Add a item

        # Ask if the user wants to add another item
        anotherYN = input("\nWould you like to enter another item (Y/N)? ").upper()

        # Validate the response
        while anotherYN not in ("Y", "YES", "N", "NO"):
            anotherYN = input("Invalid response. Please enter Y or N:").upper()

        # Break the loop if the user chooses "N" or "NO"
        if anotherYN in ("N", "NO"):
            break

    # Display the list of item
    displayItems(list)

    # Display a summary of balances
    displaySummary(list)


# Check if the script is being run directly
if __name__ == "__main__":
    main()  # Run the main function



