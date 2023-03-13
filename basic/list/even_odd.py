#seperate even or odd no. from the list

def even_odd(l):
    even=[]
    odd=[]
    for i in l:
        if(i%2==0):
            even.append(i)
        else:
            odd.append(i)
    return even,odd

l=[10,41,30,15,80]
print(even_odd(l))