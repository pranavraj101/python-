print('Number of days late :')
d=int(input())
print('Number of months late :')
m=int(input())
print('Number of year late :')
y=int(input())
fine=0
if(y>0):
    fine=10000
elif(m>0):
    fine=500*m
elif(d>0):
    fine=15*d
else:
    fine=0
print("Fine due to late submission of booK :",fine)
