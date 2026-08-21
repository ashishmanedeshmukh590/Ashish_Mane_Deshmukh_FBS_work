#WAP to  find on sum of following series using function. 

def sumpower(n):
    return sum(i**i for i in range(1, n + 1))
n = int(input('Enter the value of n:'))
sum1 = sumpower(n)

print(f'sum of series c:{sum1}')