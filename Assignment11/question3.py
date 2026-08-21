##3. WAP to sort the list according to the second element in sublist.

def sub_list_sort(li):
    li2 = []

    for i in range(len(li)):
        li2 += [li[i][1]]

        li2.sort()
    return li2
li =[[2,4],[90,100],[45,67]]

res = sub_list_sort(li)

print(res)