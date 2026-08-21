def length_ele (li):
    new = []
    
    for i in li:
        new += [len(str(i))]
    
    new.sort()
    
    print(new) 
    
li = [4000, 263, 15, 10000] 

length_ele(li)  