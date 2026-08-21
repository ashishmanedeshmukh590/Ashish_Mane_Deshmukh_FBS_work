##4.WAP to revers the list.

li =[ 10,33,43,60.70]
rev = []
for num in range(len(li)-1,-1,-1):
    rev.append(li[num])
print('original list =',li)
print('revrse list =',rev)