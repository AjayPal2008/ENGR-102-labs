# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Ajay P
# Section: ENGR 102 508
# Assignment: LAB 3
# Date: 09/09/2026

from math import *

def printresult(shape, side, area):
    '''Print the result of the calculation'''
    print(f'A {shape} with side {side:.2f} has area {area:.3f}')

side_length = float(input("Please enter the side length: "))
area_triangle = (side_length ** 2) * (3 ** 0.5) / 4
area_square = side_length ** 2
area_pentagon = (5 * side_length ** 2) / (4 * tan(pi / 5))
area_hexagon = (3 * side_length ** 2 * (3 ** 0.5)) / 2
area_Dodecagon = 3*(2+3**.5)*side_length**2

printresult("triangle", side_length, area_triangle)
printresult("square", side_length, area_square)
printresult("pentagon", side_length, area_pentagon)
printresult("hexagon", side_length, area_hexagon)
printresult("dodecagon", side_length, area_Dodecagon)#prints result of area of dodecagon