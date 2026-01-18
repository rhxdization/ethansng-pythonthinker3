import random

## Recap 1: Pseudocode (Recycling logic)
# Task: Write down the steps on how to solve the problem below

# Design pseudocode for a recycling robot that sorts items
# into bins for glass, plastic, and paper. The robot should
# check each item's material and place it in the correct bin.

# create an if statement where if material = plastic then put the plastic into the plastic bin
# else if material = glass then put the plastic into the glass bin
# else place the paper into the paper bin

## Recap 2: Variables & Mind map
# Use mindmap to think about the number of variables you need for
# the following. Then, create a program that does the following:

# You just had lunch at a sushi restaurant and have to calculate
# the total amount you have spent. Different coloured plates
# costs different as shown below:

# Red = $1
# Blue = $2
# Green = $3

# You have ordered a total of 3 red plates, 5 blue plates,
# and 4 green plates. Calculate and print the total amount you
# have spent:

# rcost = 1
# bcost = 2
# gcost = 3
# rorder = 3
# border = 5
# gorder = 4

# total = (rcost*rorder) + (bcost*border) + (gcost*gorder)
# print(total)

## Recap 3: Debugging Average Score Program
# There is a total of 3 bugs in the following program.
# Identify and fix the bugs:

# score_one = 80
# score_two = 90
# score_three = 75

# total = score_one + score_two + score_three

# average_score = total / 3

# student_name = "Alex"

# print("Average score for " + student_name + " is: " + str(average_score))

## Recap 4: If..elif..else & Flowchart

# Write a program that asks the user to input a score
# (as an integer) and then assigns a grade based on that score.
# Use the following grading scheme:

# If the score is 75 or higher, the grade is 'A'.
# If the score is between 60 and 74 (inclusive), the grade is 'B'.
# If the score is between 50 and 59 (inclusive), the grade is 'C'.
# Any score below 50 will be graded as 'Fail'.

# Use flowchart to draw out all decisions that are to be made
# before starting on your code.

score = int(input("whats your score: "))

if score >= 75:
    print("you got an A well done")
elif score >= 60:
    print("you got a B")
elif score >= 50:
    print("you got a C work harder next time")
else:
    print("you got an F, stay back after school")
