#   Author: Dayan Abdulla
#   Date: 08/24/2024
#   Homework #1 Program #1
#   Math Calculator

# print("A Simple Math Problem\n")
# result = 5 ** 2 + 7
# print(f"5 ** 2 + 7 = {result}")


def find_pair_with_sum(arr, X):
    seen = set()
    for num in arr:
        if X - num in seen:
            return (X - num, num)
        seen.add(num)
    return None

# Test the function
arr = [3, 7, 12, 6, 9, 13]
X = 13
result = find_pair_with_sum(arr, X)

