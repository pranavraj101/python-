print('Input some values seprated by commas')
values=input()
list=values.split(',')
tuple=tuple(list)
for i in range(0,len(list)):
    list[i]=int(list[i])
print("List:",list)
print("Tuple:",tuple)
l=[3,34,4,5,5,6]
print(list+l)
