print("Enter a number")
n=int(input())
if(n%2 == 0):
    print("Invalid input")
print("Odd multiples are as follow")
for i in range (1,n,2):
    if(n%i==0):
        print(i)
