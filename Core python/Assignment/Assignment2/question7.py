##7.Find the sum of three-digit number.

num = int(input("Enter three digit number: "))

sum = (num // 100) + ((num // 10) % 10) + (num % 10)

print("Sum of digits:", sum)