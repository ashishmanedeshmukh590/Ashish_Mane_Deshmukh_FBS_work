##8. WAP to check whether a number is prime or not using recursion.

def prime (num, i=2):
    if num < 2:
        return False
    if i == num:
        return True
    if num% i == 0 :
        return False
    return prime(num,i + 1)
num = int(input("Enter number: "))
if prime (num):
    print("prime number")
else:
    print("Not prime number ")