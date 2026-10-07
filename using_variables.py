# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Ajay P
# Section: ENGR 102 508
# Assignment: LAB 0
# Date: 08/24/2026
from math import*
#Reynolds Number (Re)
u = 9 # Velocity
v = 0.0015 #Kinematic Viscosity
L =  0.875 #linear dimension
print("Reynolds number is",u*L/v)
#Bragg’s Law
d = 0.03 # Distance in nm
theta = 35 # Degrees
print("Wavelength is",d*sin(theta*pi/180)*2,"nm")
#Arps equation
t = 10 # days after start in Days
qi = 100 # Initial production rate in barrels per day
Di = 2 # Initial Decline Rate
b = 0.8 # hyperbolic constant
print("Production rate is",qi/((1+b*Di*t)**(1/b)),"barrels/day")
#Tsiolkovsky rocket equation
ve = 2030 # exhaust velocity in meters per second
mo = 11000 # initial mass in Kg
mf = 8300 # final mass in Kg
print("Change of velocity is",ve*log((mo/mf),e),"m/s")