
# Matthew Thomas
# October 2nd, 2025
# P1HW1
# Create a program that does some basic math on numbers that are entered

print("This program calculates and displays travel expenses.")
ibud=int(input("Please enter your travel budget: ")) #Inital Budget
td=(input("Please enter your travel destination: ")) #Destination
gc=int(input("Please enter how much you expect to spend on gas: ")) #Gas Cost
ac=int(input("Please enter how much you expect to spend on the rent: ")) #Rent Cost
fc=int(input("Please enter how much you expect to spend on food: ")) #Food Costs
exp=(gc + ac + fc) #Total Expences
rbud=(ibud - exp)

#Display Time

print("------------Travel Expenses------------")
print("Location:", td)
print("Inital Budget:", ibud)
print()
print("Fuel:", gc)
print("Accomodation:", ac)
print("Food:", fc)
print()
print("Remaining Balance:", rbud)



#Display an explain the purpse of the program
#Declare budget
#Declare destination
#Declare Gas price
#Declare living cost
#Declare food cost
#add all expenses
#subtract expenses from budget
#Display header travel expenses
#Display location
#Display starting budget
#Display costs
#Display reamining Budget
