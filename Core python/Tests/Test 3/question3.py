##3. Write a program to accept basic salary of n emp. (n should beaccepted from user). If basic salary is below 20000 thenda=10%,ta=12% and hra=15% otherwise da=15%,ta=18% andhra=20%. Based on this calculate the total salary of each emp
#and also total salary of all emp.

n = int(input("Enter number of employees: "))

total_salary = 0

for i in range(1, n + 1):
    basic = float(input(f"Enter basic salary of employee {i}: "))

    if basic < 20000:
        da = basic * 10 / 100
        ta = basic * 12 / 100
        hra = basic * 15 / 100
    else:
        da = basic * 15 / 100
        ta = basic * 18 / 100
        hra = basic * 20 / 100

    salary = basic + da + ta + hra
    total_salary += salary

    print(f"Total salary of employee {i} = {salary:.2f}")

print(f"Total salary of all employees = {total_salary:.2f}")