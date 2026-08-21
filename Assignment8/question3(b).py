#WAP to  find on sum of following series using function. 

import math
def sum_fact(n):
    return sum(math.factorial(i) for i in range(1, n+1))
n = int(input('Enter the value of n:'))
sum1 = sum_fact(n)

print(f'sum of series b {sum1}')