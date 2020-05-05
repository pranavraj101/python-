import sys
n=int(input())  
m=n
m1=n
if(n<=1):
    print("impossible")
    sys.exit(0)
for i in range(1,n*2,2):
    for j in range(m,0,-1):
        print('*',end='')
    for k in range(1,i+1,1):
        print(" ",end="")
    for l in range(m,0,-1):
       print('*',end='')
    print()
    m-=1
    m1+=1
m=2
m1=(n*2)-3
for i in range(2,n*2,2):
    for j in range(0,m):
        print('*',end='')
    for k in range(m1,0,-1):
        print(" ",end="")
    for j in range(0,m):
        print('*',end='')
    print()
    m+=1
    m1-=2
