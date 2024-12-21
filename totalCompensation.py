#Dayan ABdulla
#11/19/24
#totalcomp


def calcCompensation(type, years):
    if type == "1": baseSalary = 70000
    elif type == "2": baseSalary = 90000
    elif type == "3": baseSalary = 120000
    tuitionReimbursement = 4000
    retirement401matching = .05
    healthInsurance = 7500
    if years <= 5:
        paidTimeOff = (baseSalary / 52) * 2
    elif years <= 10:
        paidTimeOff = (baseSalary / 52) * 3
    else:  # more than 10 years
        paidTimeOff = (baseSalary / 52) * 4
    dentalVisionInsurance = 2000
    DisbabilityLifeInsurance = 5000
    if type == "1":
        compensation = baseSalary + paidTimeOff + tuitionReimbursement + (baseSalary * retirement401matching) + healthInsurance + dentalVisionInsurance + DisbabilityLifeInsurance
    elif type == "2":
        compensation = baseSalary + paidTimeOff + tuitionReimbursement + (baseSalary * retirement401matching) + healthInsurance + dentalVisionInsurance + DisbabilityLifeInsurance
    elif type == "3":
        compensation = baseSalary + paidTimeOff + tuitionReimbursement + (baseSalary * retirement401matching) + healthInsurance + dentalVisionInsurance + DisbabilityLifeInsurance
    return compensation

### Main ###
print("\n  ---- Select Your Positoion ----\n")
print("1 - Software Engineer Level I")
print("2 - Software Engineer Level II")
print("3 - Manager Level I")
type = input("\nChoose one of the above (1-3):")
years = int(input("How many years have you been employed at the company? "))
compensation = calcCompensation(type, years)
print ("\nYour total compensation will be ${:,.2f}".format(compensation))