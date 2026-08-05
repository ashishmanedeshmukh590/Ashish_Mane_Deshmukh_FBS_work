##e. x - x2/3 + x3/5m- x4/7 +... to n term.


x = float(input('Enter value of x for series e:'))
n = int(input('Enter number of terms n for series e:'))

total_sum = 0 
denominator = 1

for i in range(1,n+1):
    term =(x ** i) /denominator
    if i % 2 == 1:
        total_sum += term
    else:
        total_sum -= term
        denominator +=2
print(f'Sum of series e :{total_sum}')
print()