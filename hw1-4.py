#   Author: Dayan Abdulla
#   Date: 08/24/2024
#   Homework #1 Program #4
#   Restaurant Ordering

import math
#user input
eggs = int(input("How many eggs did the restaurant use last month? "))
#process
cartons = eggs / 12
cartons2 = math.ceil(cartons)
cartons3 = -(-eggs // 12)
#output
print(f"Order {cartons} cartons of eggs next month")
print(f"Order {cartons2} cartons of eggs next month")
print(f"Order {cartons3} cartons of eggs next month")