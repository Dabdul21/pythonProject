#
#
def getCalcInputs():
    operation = input("Which math operation would you like to "
                      "perform (A - Add, S - Substract, M - Multiple, "
                      "or D - Division)? ").lower()
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return operation, num1, num2
def performCalc(operation, num1, num2):
    BLUE = "\033[0;34m"
    RESET = "\033[0;0m"
    if operation == "a":
        result = num1 + num2
    elif operation == "s":
        result = num1 - num2
    elif operation == "m":
        result = num1 * num2
    elif operation == "d":
        result = num1 / num2
    print(f"\n{BLUE}Result = {result:,.2f}{RESET}")

def main():
    operation, num1, num2 = getCalcInputs()
    performCalc(operation, num1, num2)

if __name__ == "__main__":
    main()
