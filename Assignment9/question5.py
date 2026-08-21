##5. WAP to find factorial using recusion.
def factorial(num):
    if num == 0 or num ==1:
        return 1
    return num * factorial (num - 1)
num = int(input("Eenter value of num: "))
res = factorial(num)
print(f'factorial of {num} is {res}')