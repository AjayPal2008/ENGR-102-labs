# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Ajay P
# Section: ENGR 102 508
# Assignment: LAB 6 indivdual
# Date: 10/01/2026
var_1 = input("Enter an integer: ")
var_2 = input("Enter another integer: ")
for i in range(1,101): # Loops through numbers 1 to 100
    if i % int(var_1) == 0 and i % int(var_2) == 0:
        print("Howdy Whoop")
    elif i % int(var_1) == 0:
        print("Howdy")
    elif i % int(var_2) == 0:
        print("Whoop")
    else:
        print(i)