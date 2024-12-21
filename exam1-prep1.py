 # David Maier
# Exam #1 Prep 1 - Fall 2024
def displayMenu():
    print("    Dearborn Apparel")
    print("")
    print(f"{'Product':15} {'Price':10}")
    print(f"{'-------':15} {'---------':10}")
    print(f"{'Pens':15} ${PENS:<10}")
    print(f"{'TShirts':15} ${TSHIRTS:<10}")
    print(f"{'Caps':15} ${CAPS:<10}")

def calcSubTutal(productName, quantity):
    if productName == "Pens":
        subTotal1 = quantity * PENS
    elif productName == "Tshirts":
        subTotal1 = quantity * TSHIRTS
    elif productName == "Caps":
        subTotal1 = quantity * CAPS
    else:
        exit("\nInvalid Product Name")
    return subTotal1

def calcDiscount(subTotal1, quantity):
    if quantity >= 1000:
        subTotal2 = subTotal1 * .90
    elif quantity >= 500:
        subTotal2 = subTotal1 * .95
    elif quantity >= 100:
        subTotal2 = subTotal1 * .97
    else:
        subTotal2 = subTotal1
    return subTotal2

def displayOrderTotal(orderTotal):
    BLUE = "\033[0;34m"
    CYAN = "\033[0;36m"
    RESET = "\033[0;0m"
    if orderTotal > 5000:
        print(f"\n{BLUE}Your order total is: ${orderTotal:,.2f}{RESET}")
    elif orderTotal > 1000:
        print(f"\n{CYAN}Your order total is: ${orderTotal:,.2f}{RESET}")
    else:
        print(f"\nYour order total is: ${orderTotal:,.2f}")

def main():
    displayMenu()
    productName = input(f"\nEnter product name to order: ").title()
    quantity = int(input("Enter quantity to order: "))
    subTotal1 = calcSubTutal(productName, quantity)
    subTotal2 = calcDiscount(subTotal1, quantity)
    orderTotal = subTotal2 * (1 + TAXES)
    displayOrderTotal(orderTotal)

if __name__ == "__main__":
    PENS, TSHIRTS, CAPS = 2.99, 24.99, 19.99
    TAXES = .06
    main()
