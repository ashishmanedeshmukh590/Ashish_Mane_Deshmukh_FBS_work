##3. WAP to  find on sum of following series using function. 

#a. 1 + 2 + 3 + 4 +.....+n
#b. 1! + 2! + 3! + 4! +.....+n!
#c. 1 ^ 1 + 2 ^ 2 + 3 ^ 3 +.....n ^ n

#a. 1 + 2 + 3 + 4 +.....+n

def sum_series(n):

 return sum(range(1, n + 1))

n = int(input('Enter the number:'))

sum1 = sum_series(n)

print(f'Enter of series a is {sum1}')