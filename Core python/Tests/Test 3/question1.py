num1 = int(input('Enter the number:'))

count = 0
num = 2
print(f'The first {num1} prime number are:')
while count < num1:
    for i in range(2,int(num**0.5)+1):
        if(num % i) == 0:
            break

    else:
        print(num,end=' ')
        count += 1
    num +=1
print()