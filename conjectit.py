t=int(input())
N=int(input())
k=0
while N:
    if(N%2==0):
        N=N/2
    else:
        N=3*N+1
        
    if(N==t):
        k=1 
        break
if(k==1):
    print("YES")
else:
    print("NO")
