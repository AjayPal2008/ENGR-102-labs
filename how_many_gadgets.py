# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Ajay P
# Section: ENGR 102 508
# Assignment: LAB 0
# Date: 09/14/2026
# Program to calculate total gadgets produced through a given day

day = int(input("Please enter a positive value for day: "))

if day <= 0:
    print("You entered an invalid number!")
elif day <= 10:
    # testing phase: flat 10 gadgets/day
    total = day * 10
    print("The sum total number of gadgets produced on day {} is {}".format(day, total))
elif day <= 50:
    # ramp-up phase: 100 from testing, plus sum of 11..day (arithmetic series)
    total = 100 + (11 + day) * (day - 10) // 2
    print("The sum total number of gadgets produced on day {} is {}".format(day, total))
elif day <= 100:
    # full speed phase: 1320 total through day 50, plus 50/day after that
    total = 1320 + (day - 50) * 50
    print("The sum total number of gadgets produced on day {} is {}".format(day, total))
else:
    # production stopped on day 101, total is frozen at the day-100 value
    total = 3820
    print("The sum total number of gadgets produced on day {} is {}".format(day, total))