#12. Write a program to create three lists of numbers, their squares
#and cubes

li = [1,2,3,4,5]
square_li = []
cube_li = []
for i in li:
    ele = i**2
    square_li.append(ele)
    ele = i**3
    cube_li.append(ele)
print('original list =',li)
print('square list =',square_li) 
print('cube list =',cube_li)