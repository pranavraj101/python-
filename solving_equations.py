a=int(input())
b=int(input())
c=int(input())
n=int(input())
x1=1
for i in range(0,n):
    y1=(c-(a*x1))/b
    #y1=format(y1,"0.2f")
    x1+=2
    if(y1==0):
        print(format(y1,"0.2f"))
    else:
        print(format(y1,"0.2f"))
