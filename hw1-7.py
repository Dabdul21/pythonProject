#   Author: Dayan Abdulla
#   Date: 08/24/2024
#   Homework #1 Program #7
#   Address
######################################

# user inputs

firstName = input("Please enter first name: ").capitalize()
lastName = input("Please enter last name: ").capitalize()
streetNumber = int(input("Please enter street number: "))  
streetName = input("Please enter street name: ")
city = input("Please enter city: ").capitalize()
state = input("Please enter state: ").upper()
zipCode = int(input("Please enter zip code: "))  
areaCode = int(input("Please enter phone area code: "))  
phonePrefix = int(input("Please enter phone prefix: "))  
phoneLast4 = int(input("Please enter phone number: "))  

# Printing customer information
print("\nCustomer Information")
print("-----------------------------")
print(f"{firstName} {lastName}")
print(f"{streetNumber} {streetName}")
print(f"{city}, {state} {zipCode}")
print(f"({areaCode}) {phonePrefix}-{phoneLast4}")
