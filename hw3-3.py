#   Author: Dayan Abdulla
#   Date: 10/3/2024
#   Homework #3 Program #3
#####################################



def quoteDisplay(dayOfWeek):
    if dayOfWeek == "Monday":
        print("Today's quote: \"Ever tried. Ever failed. No matter. Try Again. Fail again. Fail better.\" - Samuel Beckett")
    elif dayOfWeek == "Tuesday":
        print("Today's quote: \"Our greatest weakness lies in giving up. The most certain way to succeed is always to try just one more time.\" - Thomas A. Edison")
    elif dayOfWeek == "Wednesday ":
        print("Today's quote: \"It does not matter how slowly you go as long as you do not stop.\" - Confucius")
    elif dayOfWeek == "Thursday":
        print("Today's quote: \"Life is 10% what happens to you and 90% how you react to it.\" - Charles R. Swindoll")
    elif dayOfWeek == "Friday ":
        print("Today's quote: \"Start where you are. Use what you have. Do what you can.\" - Arthur Ashe")
    elif dayOfWeek == "Saturday":
        print("Today's quote: \"A good plan violently executed now is better than a perfect plan executed next week.\" - George S. Patton")
    elif dayOfWeek == "Sunday ":
        print("Today's quote: \"Do the difficult things while they are easy and do the great things while they are small. A journey of a thousand miles must begin with a single step.\" - Confucius")



def main():
    import datetime
    currentDate = datetime.datetime.now()
    dayOfWeek = currentDate.strftime("%A")
    quoteDisplay(dayOfWeek)

if __name__ == "__main__":
    main()