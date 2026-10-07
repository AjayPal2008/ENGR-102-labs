# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Ajay P
# Section: ENGR 102 508
# Assignment: LAB 0
# Date: 09/06/2026
x = 1
y = 10
z = 0

z += x
print(z)

x = 1
y = 10
z = 0

x = y
y += x
y += x
z += y
print(z)

x = 1
y = 10
z = 0

x = y
y *= x
x = 1
y += x
y += x
z += y
print(z)

x = 1
y = 10
z = 0

x = y
y *= x
x = y
y *= x
x = y
y *= x
x = y
y *= x
z += y
print(z)

x = 1
y = 10
z = 0

x = y
y *= x
z += y
z += y
z += y
z += y
z += y
z += y

y *= x

x = 1
x += 1
x += 1
x += 1
x += 1
x += 1
x += 1
x += 1

y *= x
z += y

y = 10
x = y
y += x
y += x
y += x
y += x
y += x
y += x
z += y

x = 1
x += 1
x += 1
x += 1
x += 1
z += x

print(z)