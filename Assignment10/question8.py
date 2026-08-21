##8.Write a program to create a duplicate of existing list. it should not point to Same list



original_list = [ 10, 1,30,40]

duplicate_list = []

for ele in original_list :

      duplicate_list.append (ele)



duplicate_list[0]=999.

print(f" Original list (unchanged):",original_list)
print("duplicate list (modified): ", duplicate_list)
