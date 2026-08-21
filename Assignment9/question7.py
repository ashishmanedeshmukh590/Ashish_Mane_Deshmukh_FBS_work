##7. WAP to find sum of digits using recrsion.

def sum_of_digit(num):
    if num == 0:
        return 0
        return num % 10 + sum_og_digits(num//10)
num = int(input("Enter number: "))
res = sum_of_digit(num)
print(f'sum of digit in {num} number is{res}')
