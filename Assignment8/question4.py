##4.WAP sum of all odd numbers betwwen 1 to n

def oddnum(n):
    return sum((i) for i in range(1, n + 1)if (i % 2!=0))

n = int(input('Enter the value of n:'))

res = oddnum(n)

print(res)