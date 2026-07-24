##write a program to enter P,T,R and calculate simple Interest.
P = float(input("Enter principal Amount: ")) 
T = float(input("Enter Time in years: "))
R = float(input("Entet Rate of interest: "))
SI = (P * T * R) / 100
print("simple Interest is: ", SI)