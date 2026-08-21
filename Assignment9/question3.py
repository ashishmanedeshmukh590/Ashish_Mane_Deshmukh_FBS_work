##3.Write a program to reverse a given number using recursive function.

def Reverse(num):
    if num == 0:
        return 
    print(num % 10,end='')
    Reverse (num // 10)
num = int(input('Enter the number'))
Reverse(num)