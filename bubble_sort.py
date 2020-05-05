def bubble(l):
    n=len(l)
    for i in range(n-1,0,-1):
        for j in range(0,i):
            if(l[j]>l[j+1]):
                l[j],l[j+1]=l[j+1],l[j]
    print(l)
