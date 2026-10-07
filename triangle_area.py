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
from cmath import sqrt


x_value = float(input("Enter the value of x: "))
y_value = float(input("Enter the value of y: "))

side_a = sqrt((x_value)**2 + (x_value - y_value)**2)
side_b = sqrt((x_value)**2 + (x_value+y_value)**2)
side_c = sqrt(2*(y_value)**2)
semi_perimeter = (side_a + side_b + side_c) / 2
area = sqrt(semi_perimeter * (semi_perimeter - side_a) * (semi_perimeter - side_b) * (semi_perimeter - side_c)) # Heron's Formula
print(f"The area of the triangle is {area:.3f}") # gives area of triangle
