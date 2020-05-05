c=1
n=int(input("ENter the number of students : "))
cum = 1 
su = 0
while c<=n:
    su = su + cum
    cum+=2
    c+=1
print(su)
