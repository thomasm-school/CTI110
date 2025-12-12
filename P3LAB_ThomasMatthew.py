# Matthew Thomas
# December 11th, 2025
# P3LAB
# This program allows the user to enter a money (float) value with two places after the decimal.


money = float(input("Enter the ammount of many as a float: $"))
money_in_cents = money * 100

dollars = money_in_cents // 100
money_in_cents = money_in_cents - (dollars * 100)

quarters = money_in_cents // 25
money_in_cents = money_in_cents - (quarters * 25)

dimes = money_in_cents // 10
money_in_cents = money_in_cents - (dimes * 10)

nickles = money_in_cents // 5
money_in_cents = money_in_cents - (nickles * 5)

pennies = money_in_cents // 1
money_in_cents = money_in_cents - (pennies * 1)


found_change = False
    
if dollars > 0:
    found_change = True
    name = "Dollar" if dollars == 1 else "Dollars"
    print(f"{dollars} {name}")

if quarters > 0:
    found_change = True
    name = "Quarter" if quarters == 1 else "Quarters"
    print(f"{quarters} {name}")

if dimes > 0:
    found_change = True
    name = "Dime" if dimes == 1 else "Dimes"
    print(f"{dimes} {name}")

if nickles > 0:
    found_change = True
    name = "Nickel" if nickles == 1 else "Nickels"
    print(f"{nickles} {name}")

if pennies > 0:
    found_change = True
    name = "Penny" if pennies == 1 else "Pennies"
    print(f"{pennies} {name}")

if not found_change:
    print("No Change")
