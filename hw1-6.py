#   Author: Dayan Abdulla
#   Date: 08/24/2024
#   Homework #1 Program #6
#   Quiz Grading
######################################
#user input
quiz1 = float(input("Enter score for Quiz #1:\t\t"))
quiz2 = float(input("Enter score for Quiz #2:\t\t"))
quiz3 = float(input("Enter score for Quiz #3:\t\t"))
quiz4 = float(input("Enter score for Quiz #4:\t\t"))
#hw input
hw1 = float(input("Enter score for Homework #1:\t"))
hw2 = float(input("Enter score for Homework #2:\t"))
hw3 = float(input("Enter score for Homework #3:\t"))
hw4 = float(input("Enter score for Homework #4:\t"))
hw5 = float(input("Enter score for Homework #5:\t"))
hw6 = float(input("Enter score for Homework #6:\t"))

#process
quizzes = ((quiz1 + quiz2 + quiz3 + quiz4) / 4) * .3
homework = ((hw1 + hw2 + hw3 + hw4 + hw5 + hw6) / 6 ) * .7
grade = quizzes + homework

#final output
print(" " * 25, "-" * 5)
print(f"{' ':<25} ---")
print(f"Your grade in the class is: {grade:.0f}%")