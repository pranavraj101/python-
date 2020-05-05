print("enter the country names")
cou=input()
print("enter the capitals")
cap=input()
cou=list(cou.split(" "))
cap=list(cap.split(" "))
n=len(cou)
dic={}
for i in range(0,n):
    dic[cou[i]]=cap[i]
print("enter the name of country")
x=input()
print(dic.get(x))

