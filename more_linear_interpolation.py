# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Ajay P
# Section: ENGR 102 508
# Assignment: LAB 0
# Date: 08/24/2026


from math import *

initial_distance_X = 8
initial_distance_Y = 6
initial_distance_Z = 7
initial_time = 12

final_distance_X = -5
final_distance_Y = 30.0
final_distance_Z = 9
final_time = 85

slope_X = (final_distance_X - initial_distance_X) / (final_time - initial_time)
slope_Y = (final_distance_Y - initial_distance_Y) / (final_time - initial_time)
slope_Z = (final_distance_Z - initial_distance_Z) / (final_time - initial_time)

i = 30
point = 1

while i <= 60:
    x = slope_X * (i - initial_time) + initial_distance_X
    y = slope_Y * (i - initial_time) + initial_distance_Y
    z = slope_Z * (i - initial_time) + initial_distance_Z

    print(f"At time {i:.1f} seconds:")
    print(f"x{point} = {x} m")
    print(f"y{point} = {y} m")
    print(f"z{point} = {z} m")

    if i != 60:
        print("-----------------------")

    i += 7.5
    point += 1# counts number of points needed