##2. 2. Enter number of students from user. For those many students accept marks of 5 
#subject marks from user and calculate percentage. Display all percentage and 
#average percentage of students. 

student = int(input("Enter number of students: "))

total_percentage = 0

for i in range(student):
    print(f"\nEnter marks of 5 subjects for Student {i}:")
    total = 0

    for j in range(5):
        marks = float(input(f"Subject {j + 1}: "))
        total += marks

    percentage = total / 5
    print(f"Percentage = {percentage:.2f}%")

    total_percentage += percentage

average = total_percentage / student
print(f"\nAverage Percentage = {average:.2f}%")
