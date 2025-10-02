
# Matthew Thomas
# October 2nd, 2025
# P1HW1
# Using Python's input and print functions, create a program that that can compute simple addition and exponents.

# Used Calculate Exponents
bv=int(input("Enter an integer as the base value: ")) #Base Value
exp=int(input("Enter an integer as the exponent: ")) #Exponent Value
t1=(bv ** exp) #Total Vlaue
print(bv, "raised to the power of", exp, "is", t1, "!!")

# Used to Calculate Addition and Subtraction
sti=int(input("Enter a starting integer: ")) #sti=Starting integer
addi=int(input("Enter a integer to add: ")) #addi=Added integer
subi=int(input("Enter a integer to subtract: ")) #subi=Subtracted integer
t2=(sti + addi - subi) #Second Total Value
print(sti, "+", addi, "-", subi, "is equal to", t2)