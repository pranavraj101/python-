#Sunny and Johnny together have M dollars they want to spend on ice cream. The parlor offers N flavors, and they want to choose two flavors so that they end up spending the whole amount.
#You are given the cost of these flavors. The cost of the ith flavor is denoted by ci. You have to display the indices of the two flavors whose sum is M.


print("Enter the total price that sunny and johnny")
M=int(input())
print("Enter the types of flovour offered seperated by comma")
fl=input()
fl=fl.split(",")
print("Enter the price of each flavour seperated by comma")
fl_p=input()
fl_p=fl_p.split(",")
for i in range(0,len(fl_p)):
    fl_p[i]=int(fl_p[i])

output=0
for i in range(0,len(fl_p)-1):
    for j in range(i+1,len(fl_p)):
        x=fl_p[i]+fl_p[j]
        if(M==x):
            print(i,j)
            break
