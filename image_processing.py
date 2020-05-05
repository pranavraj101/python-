n=int(input())
ip,l=[],[]
il=[]
for i in range(0,n):
    l=[]
    for j in range(0,n):  
        x=int(input())
        l.append(x)
        if(i==0):
            il.append(x)
    ip.append(l)
print(ip)
for i in range(1,n-1):
    il.append(ip[i][n-1])
x=ip[n-1]
for i in range(n-1,-1,-1):
    il.append(x[i])
for i in range(n-2,0,-1):
    il.append(ip[i][0])
print(il)
print("1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9 and 5")
print("3 2 8 4 5 6 7 16 1 10 11 12 13 9 15 14")
for i in range(0,len(il)-2,2):
    il[i],il[i+2]=il[i+2],il[i]
print(il)
