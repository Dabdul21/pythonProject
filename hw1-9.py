#   Author: Dayan Abdulla
#   Date: 08/24/2024
#   Homework #1 Program 9
# hw1-9.py


#CONST
taxRate = 0.06

#input
item1 = float(input("Enter the price of the first item "))
item2 = float(input("Enter the price of the second item "))
item3 = float(input("Enter the price of the third item "))

#Calculate subtotal

subtotal = item1 + item2 + item3

#calculate sales tax and total

salesTax = subtotal * taxRate
total = subtotal + salesTax

#display
print(f"Subtotal: ${subtotal: .2f}")
print(f"Sales Tax (6%): ${salesTax:.2f}")
print(f"Total: ${total:.2f}")