# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Ajay P
# Section: ENGR 102 508
# Assignment: LAB 5 individual
# Date: 09/24/2026
# Program to calculate the heat flux based on excess temperature using the boiling curve data points and interpolation

import math



Point_A = (1.3, 1000)
Point_B = (5, 7000)
Point_C = (30, 1.5e6)
Point_D = (120, 2.5e4)
Point_E = (1200, 1.5e6)

# Ask the user for an input value
x1 = float(input("Enter the excess temperature: "))

if x1 < Point_A[0] or x1 > Point_E[0]:
    print("Surface heat flux is not available")

else:
    
    if x1 <= Point_B[0]:
        x0, y0 = Point_A
        x2, y2 = Point_B

    elif x1 <= Point_C[0]:
        x0, y0 = Point_B
        x2, y2 = Point_C

    elif x1 <= Point_D[0]:
        x0, y0 = Point_C
        x2, y2 = Point_D

    else:
        x0, y0 = Point_D
        x2, y2 = Point_E

   
    Slope = math.log(y2 / y0) / math.log(x2 / x0)

  
    Result = y0 * (x1 / x0) ** Slope

    # Values tested and their expected outputs:
   
    # Test 1 at delta TE = 1.3 output should be: 1000 W/m^2
    # Test 2 at delta TE = 5 output should be: 7000 W/m^2
    # Test 3 at delta TE = 30 output should be: 1.5x10^6 W/m^2
    # Test 4 at delta TE = 120 output should be: 2.5x10^4 W/m^2
    # Test 5 at delta TE = 2 output should be: approximately 1863 W/m^2
    # Test 6 at delta TE = 15 output should be: approximately 188079 W/m^2
    # Test 7 at delta TE = 60 output should be: approximately 193649 W/m^2
    # Test 8 at delta TE = 500 output should be: approximately 316241 W/m^2
    # Test 9 at delta TE < 1 output should be: Surface heat flux is not available
    # Test 10 at delta TE > 1200 output should be: Surface heat flux is not available
        
   

    print(f"The surface heat flux is approximately {round(Result)} W/m^2")

