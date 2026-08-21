##3. WAP to find the second largest element in the list.

li =[2,45,33,23,90,67,4]
max =li[0]
second_largest_ele = li [0]
for num in range(1,len(li)):
  if(li[num] > max):
    second_largest_ele = max
    max = li[num]
  elif li[num] > second_largest_ele and li[num]!= max:
    second_largest_ele = li[num]
print(f' second largest element in list is {second_largest_ele}')