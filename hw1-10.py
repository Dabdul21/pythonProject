#   Author: Dayan Abdulla
#   Date: 08/24/2024
#   Homework #1 Program 10
# hw1-10.py

#input
amountOwed = float(input("Enter amount owed: "))
amountPaid = float(input("Enter the amount paid: "))

#calculate change
change = amountOwed - amountPaid

#Display
print(f"Amount Owed: ${amountOwed:<20.2f}")
print(f"Amount Paid: ${amountPaid:<20.2f}")

#Blue text
print("\033[94m" + f"Customer receives ${change:.2f} change." + "\033[0m")