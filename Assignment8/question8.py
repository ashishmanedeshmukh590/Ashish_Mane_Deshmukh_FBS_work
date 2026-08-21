##8.WAP find reverse of a number

def reverse(n):
    rev = 0
    while(n> 0):
        d = n % 10
        rev = rev * 10+d

        n//= 10
    return rev
n= int(input('Enter the number:'))
res = reverse(n)
print(f'the reverse number of {n} is {res}')