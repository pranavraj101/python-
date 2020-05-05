n=int(input())
i=0
m=n
while n:
    d=n%10
    n=n//10
    if(d!=0):
        if(m%d==0):
            i=i+1
            if(i>1):
                print(",",d,end="")
            else:
                print(d,end="")
if(i==0):
    print("No factors")
