##6.Write a program to remove duplicates from list.


li = [1, 2, 2, 3, 3, 4, 5]


li2 = []


for ele in li:
    if ele not in li2:
        li2.append(ele)


print(f"Original list = {li}")
print(f"List after removing duplicates = {li2}")