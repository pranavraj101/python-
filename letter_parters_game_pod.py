import sys
s=input()
c,k,b=0,0,0
pre,post=[],[]
l=len(s)
if(l%2!=0):
    print("Lost")
    sys.exit(0)
else:
    c=l//2
for i in range(0,len(s)-1):
    x=chr(ord(s[i])+13)
    for j in range(i+1,len(s)):
        print(k,x,s[j])
        if(s[j]==x):
            k+=1
            pre.append(s[i])
            post.append(s[j])
print(pre,post)
l=s
for i in pre:
    x=l[l.index(i)+1]
    print(i,x,chr(ord(x)+13))
    if(i==chr(ord(x)+13)):
        b==1
    else:
        l1=post
        for m in post:
            print(m,chr(ord(x)+13))
            if(chr(ord(x)+13)==m):
                l1.remove(m)
                break
            print(m,l1)
        for j in l1:
            if(chr(ord(x)+13)):
                b==1    
if(c==k and b==1):
    print("Won")
else:
    print("Lost")
