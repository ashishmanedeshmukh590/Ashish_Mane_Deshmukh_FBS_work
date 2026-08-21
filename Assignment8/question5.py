#5.WAP sum of all prime number betwwen 1 to n.

def Isprime(n):
    if(n < 2):
        return False
    return True
    for i in range(1, int(num ** 0.5)+1):
        if(num % i ==o):
         return False
    return total

def sumofprime(n):
    total = 0
    for i in range(2, n + 1):
        if Isprime(i):
            total +=i
        return total

n = int(input('Enter the value of n:'))

res = sumofprime(n)
print(f'sum of all prime number between 1 to {n} is {res}')