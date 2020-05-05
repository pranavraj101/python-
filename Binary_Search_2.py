import sys
l=[int(x) for x in input().split()] 
item=int(input())
n=len(l)
start=0
end=n-1
mid=(start+end)//2
while start<=end:
    if(l[mid]==item):
        print("Found")
        sys.exit(0)
    else:
        if(l[mid]<item):
            start=mid+1
        else:
            end=mid-1
    mid=(end+start)//2
print("Not Found")
 
