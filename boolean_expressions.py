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
# Date:         11 September 2026

############ Part A ############
response_a = input("Enter True or False for a: ").lower()
a = response_a == "t" or response_a == "true"

response_b = input("Enter True or False for b: ").lower()
b = response_b == "t" or response_b == "true"

response_c = input("Enter True or False for c: ").lower()
c = response_c == "t" or response_c == "true"

############ Part B ############
print(f"a and b and c: {a and b and c}")
print(f"a or b or c: {a or b or c}")

############ Part C ############
XOR1 = (a and not b) or (not a and b)
print(f"XOR: {XOR1}")

odd_count = (a and not b and not c) or (not a and b and not c) or (not a and not b and c) or (a and b and c)
print(f"Odd number: {odd_count}")

############ Part D ############
Complex_1 = (not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b)
Complex_2 = (not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or (a and b and c) or (a and ((b and not c) or (not b))))

Simple_1 = (not b) or (not a and not c)
Simple_2 = (a or ((not b) and c))

print(f"Complex 1: {Complex_1}")
print(f"Simple 1: {Simple_1}")
print(f"Complex 2: {Complex_2}")
print(f"Simple 2: {Simple_2}")