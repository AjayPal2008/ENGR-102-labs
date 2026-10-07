# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Micah Kadiri
#               Benjamin Hatch
#               Ajay Palanisamy
#               Hudson Dobbs
# Section:      508
# Assignment:   Lab Topic 4 (Team)
# Date:         14 September 2026

from operator import eq

a = int(input("Please enter the coefficient A: "))
b = int(input("Please enter the coefficient B: "))
c = int(input("Please enter the coefficient C: "))

equation = ""

if a != 0:
    if abs(a) == 1:
        a_term = "x^2"
    else:
        a_term = str(abs(a)) + "x^2"
        
    if a < 0:
        equation = "- " + a_term
    else:
        equation = a_term
    
if b != 0:
    if abs(b) == 1:
        b_term = "x"
    else:
        b_term = str(abs(b)) + "x"
        
    if equation == "":
        if b < 0:
            equation = "- " + b_term
        else: 
            equation = b_term
    elif b < 0:
        equation += " - " + b_term
    else: 
        equation += " + " + b_term
    
if c != 0:
    if equation == "":
        equation = str(c)
    elif c < 0:
        equation += " - " + str(abs(c))
    else: 
        equation += " + " + str(c)
        
if equation == "":
    equation = "0"
    
print("The quadratic equation is", equation, "= 0") # Output for equation
    