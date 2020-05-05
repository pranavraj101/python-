import math
print('Enter the number to check whether it is alam number or not')
n=int(input())
a=0
s=n*n
m=n
new=0
news=0
b=0
while (s!=0):
    a=s%10
    s=s//10
    new=new*10+a
    print(a,new,s)
print('end')
    
news=int(math.floor(math.sqrt(new)))
print(news)

while (news!=0):
    a=news%10
    news=news//10
    b=b*10+a
    print(a,news,b)
print("end")
if(m==b):
    print("ALAM NUMBER")
else:
    print('NOT A ALAM NUMBER')
