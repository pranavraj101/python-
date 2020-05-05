print("Enter the number the number to find its factorial")
n=int(input())
fact=1
for i in range(1,n+1,1):
    fact=fact*i
    print(fact)
print("end")
print(fact)
