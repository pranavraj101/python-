l=[int(x) for x in input().split()]
for i in range(1,len(l)):
    j=i-1
    while j>=0 and l[j]>l[j+1]:
        l[j],l[j+1]=l[j+1],l[j]
        j=j-1
        print(l,i,j)
    print("")
print(l)
