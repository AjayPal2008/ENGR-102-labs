# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Ajay P
# Section: ENGR 102 508
# Assignment: LAB 0
# Date: 09/14/2026

# Program to calculate the roots of a quadratic equation

# Program to calculate the roots of a quadratic equation

A = float(input("Please enter the coefficient A: "))
B = float(input("Please enter the coefficient B: "))
C = float(input("Please enter the coefficient C: "))

discriminant = B**2 - 4*A*C

if A == 0 and B == 0:
    print("You entered an invalid combination of coefficients!")
elif A == 0:
    # linear equation: Bx + C = 0
    root = -C / B
    print("The root is x = ", root)
elif discriminant < 0:
    # complex roots
    real_part = -B / (2*A)
    imag_part = (-discriminant)**0.5 / (2*A)
    print("The roots are x = {} + {}i and x = {} - {}i".format(real_part, imag_part, real_part, imag_part))
elif discriminant == 0:
    root = (-B) / (2*A)
    print("The root is x =", root)
else:
    root1 = (-B + discriminant**0.5) / (2*A)
    root2 = (-B - discriminant**0.5) / (2*A)
    print("The roots are x = {} and x = {}".format(root1, root2))# outputting roots
    
