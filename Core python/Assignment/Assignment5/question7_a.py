##7. Write a program to solve the following series : 
#a. 1! + 2! + 3! + 4! + …..n!

n = int(input('Enter n for series a:'))
total_sum = 0
fact =1
for i in range(1,n+1):
    fact *=i
    total_sum += fact
print(f'sum of series a:{total_sum}')
print()
