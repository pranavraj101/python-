print("Enter a number to check whether it is ")
n=int(input())
digit=0
factn=0
f=1
m=n
while(n!=0):
    digit=n%10
    n=n//10
    for i in range(1,digit+1):
        f=f*i
        #print(f)
    factn=factn+f
    f=1
    #print(digit,factn,n)
if(factn==m):
    print("STRONG NUMBER")
else:
    print('NOT A STROMG NUMBER')
