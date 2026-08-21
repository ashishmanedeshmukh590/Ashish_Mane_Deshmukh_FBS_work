##.11 Check Armstrong Number
def count_digits(num):
    count = 0
    temp = num

    while temp > 0:
        count += 1
        temp = temp // 10

    return count


def is_armstrong(num):
    digits = count_digits(num)
    temp = num
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp = temp // 10

    return total == num


num = int(input("Enter a number: "))

if is_armstrong(num):
    print(num, "is an Armstrong number.")

else:
    print(num, "is not an Armstrong number.")


