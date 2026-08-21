#9. Write a program of having n number of elements in the list and find out even
#and odd elements in that list and then create two separate lists which will have
#even elements and other will have odd elements.

n = int(input("Enter the number of elements(n):"))
li=[]
for i in range(n):
    ele=int(input(f"enter element{i+1}:"))
    li.append(ele)

even_list=[]
add_list=[]
count = 0
for ele in li:
    if ele % 2 == 0:
        even_list.append(ele)
        count += 1
    else:
        add_list.append(ele)
        count += 1
print("Total even element in list =",even_list) 
print("Total add element in list =",add_list)