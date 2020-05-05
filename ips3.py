n=int(input())
id=input()
id.split(' ')
#print(id)
id1=set(id)
n1=0
fl={}
for i in range(0,n):
    l=input()
    l.split(' ')
    l1=set(l)
    a=l1.intersection(id1)
    if(n1<len(a)):
        n1=len(a)
        fl=a
    print(l,l1,a,n1,fl)
fl=list(fl)
fl.remove(" ")
for i in range(0,len(fl)):
    print(fl[i],end=' ')
print()
print()
