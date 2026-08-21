##9.WAP to check if enterd number is pallindrome number or not

def pallindrome(n):

    temp = n 
    rev = 0

    while(temp>0):
        d = temp % 10
        rev = rev * 10+d
        temp //=10
    if (n == rev):
        print('the given number is pallindrome')
    else:
        print('the given number is not pallindrome')

n = int(input('Enter the number'))
pallindrome(n)