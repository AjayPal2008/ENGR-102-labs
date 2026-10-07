# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Ajay P
# Section: ENGR 102 508
# Assignment: LAB 0
# Date: 09/14/2026
num_1 = float(input("Enter number 1: "))
num_2 = float(input("Enter number 2: "))
num_3 = float(input("Enter number 3: "))

if num_1 >= num_2 and num_1 >= num_3:
    largest = num_1
elif num_2 >= num_1 and num_2 >= num_3:
    largest = num_2
else:
    largest = num_3

print("The largest number is", largest)#outputs largest number
