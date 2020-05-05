print("Enter the sales details of items in sections 1 seperated by comma")
d1=input()
d1=d1.split(",")
print("Enter the sales details of items in sections 2 seperated by comma")
d2=input()
d2=d2.split(",")
d1.sort()
d2.sort()


detail=d1+d2

print(detail)
