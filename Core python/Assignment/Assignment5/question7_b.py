##b. N + N^2 + N^3+N^4 …..+N^N (here ^ means exponent) 

n = int(input('Enter n:'))

sum = 0
for i in range(1,n+1):
    sum += n ** i

    print('sum : ',sum)