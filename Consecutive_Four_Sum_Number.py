n=int(input())
k=0
x=0
for i in range(1,n-3):
    j=i
    if (j+(j+1)+(j+2)+(j+3))==n :
        k=1
        x=j
        break
if(k==1):
    print(k)
    print(i)
elif(k==0):
    print(k)

