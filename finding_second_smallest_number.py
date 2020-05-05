n=int(input())
fl=[]
for i in range(0,n):
        name = input()
        score = float(input())
        l=[]
        l.append(score)
        l.append(name)
        fl.append(l)
fl.sort()
print(fl)
x=min(fl)
m=fl.count(x)
print(x,m)
for i in fl:
        if(x[0]==i[0]):
                fl.remove(i)
x=min(fl)
print(fl)
print(x)
for i in range(0,len(fl)):
        print(fl,x)
        if(x[0]==fl[i][0]):
                print(fl[i][1])
