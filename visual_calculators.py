print("Visual Calculator for Programmers")
print("Enter the data as per the operation you have to perform")
print("1.for ADDITION")
print("2.for SUBTRACTION")
print("3.for MULTIPLICATION")
print("4.for DIVISION")
c=int(input())
print("Enter to number for the above mentioned operation")
a=int(input())
b=int(input())
result=0
if(c==1):
    result= a+b
elif(c==2):
    result=a-b
elif(c==3):
    result=a*b
elif(c==4):
    result=a/b
else:
    print("Invalid input")
if(result != 0):
    print("The required output :",result)
    
