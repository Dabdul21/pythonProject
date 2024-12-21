#   Author: Dayan Abdulla
#   Date: 10/31/2024
#   diagnose
#####################################
import os
def diagnosticMenu():
    while True:
        print("\n   METROPOLITIAN MEDICAL CENTER")
        print("         IT Services HelpDesk")
        print("          Diagnostic Utility")
        print("----------------------------------")
        print("1. Diagnose PC Power Problem")
        print("2. Diagnose PC Monitor Problem")
        print("3. Diagnose Network Problem")
        print("4. Return to the Main Menu")
        diagChoice = input("\nPlease enter choice (1-4): ")

        if diagChoice == "1":
            print("\n Diagnose power issue \n")
            pause=input ("Press any key to open diagnostic chart")
            os.startfile("diagnose_power.pdf")
        elif diagChoice == '2':
            print("\nDiagnose PC Monitor Problem.")
            input("This is a stub. Press [Enter] to continue.")
        elif diagChoice == '3':
            print("\nDiagnose Network Problem.")
            input("This is a stub. Press [Enter] to continue.")
        elif diagChoice == '4':
            break
        else:
            print("\nInvalid menu choice. Please enter a menu choice of 1-4.")