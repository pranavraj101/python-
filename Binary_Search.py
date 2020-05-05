l=[int(x) for x in input().split()]
find=int(input())
n=len(l)
low=0
high=n-1
found=False
mid=(low+high)//2
while high>=low and not found:
    if(l[mid]==find):
        print(l[mid],n)
        found=True
    else:
        if(n<l[mid]):
            high=mid-1
        else:
            low=mid+1
    mid=(low+high)//2
print(found)
