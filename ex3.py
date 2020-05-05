#Watson gives Sherlock an list of N numbers. Then he asks him to determine if there exists an element in the list such that the sum of the elements on its left is equal to the sum of the elements on its right. If there are no elements to the left/right, then the sum is considered to be zero. 
l=input()
list1=l.split(',')
l_sum=0
r_sum=0
n=len(list1)
for i in range(0,n):
    list1[i]=int(list1[i])
for i in range(0,n):
    if(i==0):
        l_sum=0
    else:
        for j in range(0,i):
            l_sum=l_sum+list1[j]
    if(i==n-1):
        r_sum=0
    else:
        for j in range(i+1,n):
            r_sum=r_sum+list1[j]
    
    if(l_sum==r_sum):
        print(list1[i])
        break
    l_sum=0
    r_sum=0
