# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Ajay P
# Section: ENGR 102 508
# Assignment: LAB 0
# Date: 08/24/2026
from math import*
print("This shows the evaluation of (1-cos(x))/x^2 evaluated close to x=0")
print("my guess is",.5)
x = 1
for i in range(0,8):# repeatedly checks limit
    y = x/10**i
    print((1- cos(y))/y**2)
    i+=1
print("\nmy guess was correct!!")
