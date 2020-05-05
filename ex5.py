#Given a list of integer values, find the fraction of count of positive numbers, negative numbers and zeroes to the total numbers. Print the value of the fractions correct to 3 decimal places. 
list1=input()
list1=list1.split(",");
for i in range(0,len(list1)):
    list1[i]=int(list1[i])
l=len(list1)
p=0
n=0
z=0
for i in list1:
    if(i<0):
        n=n+1
    elif(i>0):
        p=p+1
    else:
        z=z+1

n=n/l
p=p/l
z=z/l

print(n)
print(p)
print(z)
