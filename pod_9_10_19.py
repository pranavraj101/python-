n=int(input())
l=input()
l.split(" ")
k=0
for i in range(0,n):
    x=int(l[i])
    print(type(x))
    k.extend(x)
sum=0
for i in l:
    sum=sum+i
sum.ceil()
print(int(sum))
