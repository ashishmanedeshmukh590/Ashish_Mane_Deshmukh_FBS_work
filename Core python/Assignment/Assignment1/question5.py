##write a program to enter P, t , R and calculate Compound Interest.
P = float(input("Enter Principal Amount: "))
T = float(input("Enter Time in years: "))
R = float(input("Enter Rate of Interest: "))
CI = P * (1 + R/100) ** T - P
print("Compound Interest is: ", CI)
