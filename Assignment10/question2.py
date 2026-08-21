##2.Write a program minimum igram to find maximum and element in a list.


li= [11, 28, 280, 44, 8,3]
max = li[0]
min = li[0]
for i in range(1,len(li)):
    if(li[i] > max):
        max = li[i]
    elif(li[i] < min):
        min = li[i]
print(f'Minimum element : {min}')
print(f'Maximum element: {max}')


 