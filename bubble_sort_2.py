l=[int(x) for x in input().split()]
n=len(l)
for x in range(n-1,0,-1):
    for i in range(0,x):
        if(l[i]>l[i+1]):
            l[i],l[i+1]=l[i+1],l[i]
print(l)
