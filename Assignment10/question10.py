#10. Write a program to remove all occurrences of a given element in the list.

li = [10,22,6,6,89,11,16]
print("original list with occurences:",li)
num = int(input("Enter the element to remove comletely:"))
filtered_list = []
for i in li:
    if i!= num:
        filtered_list.append(i)
print("List after removing all occrences:",filtered_list)