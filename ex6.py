#Given N integers, count the number of pairs of integers whose difference is K.
print("Input the numbers seperated by comma ")
nums=input()
nums=nums.split(',')
print("Enter the number for difference ")
k=int(input())
c=0
for i in range(0,len(nums)):
    nums[i]=int(nums[i])
for i in range(0,len(nums)-1):
    for j in range(i+1,len(nums)):
        if abs(nums[j]-nums[i])==k:
            c=c+1
            
print(c)
