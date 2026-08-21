##3. Write a program to check if given number is Armstrong or not using recursive function.

def Armsrrong(num,power):
    if num == 0:
        return 0
    return (num % 10)** power + Armsrrong(num // 10,power)

num = int(input('Enter the number:'))
digit = len(str(num))

if Armsrrong(num,digit) == num:
    print('Armstrrong number')
else:
    print('Not armstrong number')