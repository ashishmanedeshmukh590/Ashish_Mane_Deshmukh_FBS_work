##4. WAP to print Armstrong number within a given range 

start = int(input("Enter starting range: "))
end = int(input("Enter ending range: "))

print("Armstrong Numbers:")

for num in range(start, end + 1):
    temp = num
    dig = len(str(num))
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** dig
        temp //= 10

    if total == num:
        print(num)