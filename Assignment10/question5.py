##5.Accept number from user and check if this element is present in the list or not. Also tell how many times it is present in the list..

li  =[11,12,2,24,4,77,10,9,2]
num = int(input("Enter number :"))
count =li.count(num)
if count > 0:
    print(f'{num} is present in list{count} times')
else:
    print(f'{num} is not present in list')