#Dayan Abdulla
#09/28/2024
#HW 2 extra credit 4
#############################
from datetime import datetime

import calendar

def displayDate():
    today = datetime.today()
    dayWeek = today.strftime("%A") #shows current day of week using strftime
    numDays = calendar.monthrange(today.year, today.month)[1] #shows the # of days in month

    print(f"Today is: {dayWeek}")
    print(f"Number of days in the current month: {numDays}")

def main():
    displayDate()


if __name__ == "__main__":
    main()