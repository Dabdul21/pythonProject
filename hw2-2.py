#   Author: Dayan Abdulla
#   Date: 09/10/2024
#   Homework #2 Program #2
#####################################

#Const, Process, Output
def calFinalBill(restaurantBill):
    SENIOR_DISCOUNT = .1  # 10% discount
    finalBill = restaurantBill * (1 - SENIOR_DISCOUNT)
    # output
    print(f"Your final bill after discount is: ${finalBill:,.2f}")

#USER Input Function Call
def main():
    billAmount = float(input("Enter your bill amount: $ "))
    calFinalBill(billAmount)

if __name__ == "__main__":
    main()