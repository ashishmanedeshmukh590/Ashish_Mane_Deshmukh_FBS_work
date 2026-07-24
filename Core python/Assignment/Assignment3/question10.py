##10. Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18) 

gender = input("Enter Gender (male/female): ").lower()
age = int(input("Enter Age: "))

if (gender == "male" and age >= 21) or (gender == "female" and age >= 18):
    print("Eligible for Marriage")
else:
    print("Not Eligible")