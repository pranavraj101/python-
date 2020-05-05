l=[int(x) for x in input().split()]
for i in range(0,len(l)-1):
    for j in range(len(l)-2,0,-1):
        if(l[j]>l[j+1]):
            l[j],l[j+1]=l[j+1],l[j]
print(l)
