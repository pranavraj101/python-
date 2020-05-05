a=[int(x)for x in input().split()]
p=0
n=0
z=0
for i in a:
    if i<0:
        n+=1
    elif i==0:
        z+=1
    elif i>0:
        p+=1
print(p,n,z)
