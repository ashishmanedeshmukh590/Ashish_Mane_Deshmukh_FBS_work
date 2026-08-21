##1. #Write a program to find sum of following series using recursive functions:

# i. 1! + 2! + 3! + 4! +..... + n!

# Note : For fact and sum two recursive functions


def Fact(n):
    if n==0 or n==1:
        return 1
    return n *  Fact(n-1)
def SumFact(n):
    if n == 1:
        return Fact(1)
    return Fact(n) + SumFact(n-1)
n =int(input('Enter value of n:'))
res = SumFact(n)
print('Sum :',res)