def Selection(l):
    n=len(l)
    for i in range(0,n):
        min=i
        for j in range(i+1,n):
            if(l[min]>l[j]):
                min=j
        l[min],l[i]=l[i],l[min]
    print(l)
