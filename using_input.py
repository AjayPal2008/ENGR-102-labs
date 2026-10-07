# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Ajay P
# Section: ENGR 102 508
# Assignment: LAB 3
# Date: 09/09/2026

from math import *

print("This program calculates the Reynolds number given velocity, length, and viscosity")

# Reynolds Number (Re)
u = float(input("Please enter the velocity (m/s): "))
L = float(input("Please enter the length (m): "))
v = float(input("Please enter the viscosity (m^2/s): "))

print("Reynolds number is", round(u * L / v))

print()

# Bragg's Law
print("This program calculates the wavelength given distance and angle")

d = float(input("Please enter the distance (nm): "))
theta = float(input("Please enter the angle (degrees): "))

wavelength = 2 * d * sin(theta * pi / 180)
print("Wavelength is", format(wavelength, ".4f"), "nm")

print()

# Arps equation
print("This program calculates the production rate given time, initial rate, and decline rate")

t = float(input("Please enter the time (days): "))
qi = float(input("Please enter the initial rate (barrels/day): "))
Di = float(input("Please enter the decline rate (1/day): "))

b = 0.8
production_rate = qi / ((1 + b * Di * t) ** (1 / b))

print("Production rate is", format(production_rate, ".2f"), "barrels/day")

print()

# Tsiolkovsky rocket equation
print("This program calculates the change of velocity given initial mass, final mass, and exhaust velocity")

mo = float(input("Please enter the initial mass (kg): "))
mf = float(input("Please enter the final mass (kg): "))
ve = float(input("Please enter the exhaust velocity (m/s): "))

delta_v = ve * log(mo / mf)

print("Change of velocity is", format(delta_v, ".1f"), "m/s")
