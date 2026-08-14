##2.2. Write a program to calculate the sum of following serieswhere n is input by user.
#1/1! + 2/2! + 3/3! + 4/4! + ... N/N!


n = int(input("Enter the value of N: "))

factorial = 1
sum = 0

for i in range(1, n + 1):
    factorial *= i
    sum += i / factorial

print("Sum of the series =", sum)



