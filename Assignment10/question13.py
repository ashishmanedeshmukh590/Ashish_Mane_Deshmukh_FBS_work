#13 . Write a program to print list after removing even numbers.

li =[2,33,7,12,90,30,55]
removed_li=[]
for i in li:
    if i % 2!= 0:
     removed_li.append(i)
print('original list =',li)
print('list after removing even number from original list =',removed_li)