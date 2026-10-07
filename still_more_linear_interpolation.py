# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Micah Kadiri
#               Benjamin Hatch
#               Ajay Palanisamy
#               Hudson Dobbs
# Section:      508
# Assignment:   Lab Topic 3 (Team)
# Date:         8 September 2026
from math import *

initial_time = float(input("Enter time 1: "))
initial_distance_X = float(input("Enter the x position of the object at time 1: "))
initial_distance_Y = float(input("Enter the y position of the object at time 1: "))
initial_distance_Z = float(input("Enter the z position of the object at time 1: "))

final_time = float(input("Enter time 2: "))
final_distance_X = float(input("Enter the x position of the object at time 2: "))
final_distance_Y = float(input("Enter the y position of the object at time 2: "))
final_distance_Z = float(input("Enter the z position of the object at time 2: "))

slope_X = (final_distance_X - initial_distance_X) / (final_time - initial_time)
slope_Y = (final_distance_Y - initial_distance_Y) / (final_time - initial_time)
slope_Z = (final_distance_Z - initial_distance_Z) / (final_time - initial_time)#Calculates Z slope

i = initial_time
print()
while i <= final_time:
    x = slope_X * (i - initial_time) + initial_distance_X
    y = slope_Y * (i - initial_time) + initial_distance_Y
    z = slope_Z * (i - initial_time) + initial_distance_Z

    print(f"At time {i:.2f} seconds the object is at ({x:.3f}, {y:.3f}, {z:.3f})")

    i += (final_time - initial_time) / 4