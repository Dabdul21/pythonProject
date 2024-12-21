import random

num = random.randint(1,5)
working = True
guess = 0

print("You will never guess the correct number 1-5: " , end = '')
while working:
    guess = input()
    if not guess.isdigit():
        print("Invalid Ony DIGITS! " )
        break
    elif int(guess) < num:
        print("Too low try again: " , end = '' )
    elif int(guess) > num:
        print("Too high try again: " , end = '')
    else:
        print("Correct num is " + guess)
        working = False
