# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Micah Kadiri
#               Benjamin Hatch
#               Ajay Palanisamy
#               Hudson Dobbs
# Section:      508
# Assignment:   Lab Topic 3 (Team)/(optional)
# Date:         8 September 2026

import math

print("Part 1")
height = float(input("Enter the height of the door: "))
width = float(input("Enter the width of the door: "))

radius = width / math.sqrt(2)
rise = radius - width / 2

rectangle_area = width * (height - rise)
arc_area = (math.pi * radius**2 / 4) - (width * radius / 2)

door_area = rectangle_area + arc_area

print(f"The area of the door is {door_area:.2f}")

print()
print("Part 2")
height_pyramid = float(input("Enter the height of the pyramid: "))

surface_area = 2 * (1 + math.sqrt(3)) * height_pyramid**2

print(f"The surface area of the pyramid is {surface_area:.2f}")

print()
print("Part 3")
triangle_area = float(input("Enter the area of a triangle: "))

a = math.sqrt(4 * triangle_area / math.sqrt(3))

b = math.sqrt(
    2 * a**2 + 2 * math.sqrt(a**4 - 4 * triangle_area**2)
)

c = (2 * triangle_area) / b

d = math.sqrt(b**2 + c**2)

e = math.sqrt(
    a**2 + d**2 - 2 * math.sqrt(a**2 * d**2 - 4 * triangle_area**2)
)

print(f"The equilateral triangle has sides with length {a:.2f}")
print(f"The isosceles triangle has two sides with lengths {a:.2f} and one side with length {b:.2f}")
print(f"The right triangle has sides with lengths {b:.2f}, {c:.2f}, and {d:.2f}")
print(f"The arbitrary triangle has sides with lengths {a:.2f}, {d:.2f}, and {e:.2f}")