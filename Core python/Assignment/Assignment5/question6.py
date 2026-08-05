##6. Write a program to print first n prime numbers. 

number = int(input("Enter n: "))

count = 0
num = 2

while count < num:

    for i in range(2, int(num ** 0.5) + 1):
        if (num % i) == 0:
            break

    else:
        print(num, end=" ")
        count += 1

    num += 1
print()