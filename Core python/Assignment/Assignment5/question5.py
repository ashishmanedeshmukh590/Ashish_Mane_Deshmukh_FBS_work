##5. Write a program to print prime numbers between 1 to 100. 

print("Prime numbers from 1 to 100:")

for i in range(2, 101):
    prime = True

    for j in range(2, int(i ** 0.5) + 1):
        if (i % j)  == 0:
            break

    else:
        print(i, end=" ")