#7.WAP to find sum of digits of a number

def sumofdigit(num):
    sum = 0
    while(num>0):
        digit = num % 10
        sum += digit 
        num = num // 10
    return sum
num = int(input('Enter the number:'))
res = sumofdigit(num)
print(f'sum of ditig in {num} is {res}')