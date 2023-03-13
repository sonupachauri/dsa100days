#avg or mean of list
def avgMean(l):
    sum=0
    for i in l:
        sum = sum+i
        n=len(l)
    return  sum/n

l=[10,20,30,40]
print(avgMean(l))