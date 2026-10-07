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
# Date:         11 September 2026
#

nickel = 0.05
quarter = 0.25
dime = 0.10
penny = 0.01

x = float(input("How much did you pay? "))
y = float(input("How much did it cost? "))

change = round(x - y, 2)
change_cents = round(change * 100)

if change_cents < 0:
    print("Error: amount paid is less than the cost.")
else:
    quarters, change_cents = change_cents // 25, change_cents % 25
    dimes, change_cents = change_cents // 10, change_cents % 10
    nickels, change_cents = change_cents // 5, change_cents % 5
    pennies = change_cents

    print(f"You received ${change:.2f} in change. That is...")# prints output for change

    if quarters == 1:
        print("1 quarter")
    else:
        if quarters != 0:
            print(f"{quarters}", "quarters")
    if dimes == 1:
        print("1 dime")
    else:
        if dimes != 0:
            print(f"{dimes}", "dimes")
    if nickels == 1:
        print("1 nickel")
    else:
        if nickels != 0:
            print(f"{nickels}", "nickels")
    if pennies == 1:
        print("1 penny")
    else:
        if pennies != 0:
            print(f"{pennies}", "pennies")