import sys
pan=input()
l=len(pan)
k=0
if (l!=10):
    print("Invalid")
    sys.exit(0)

for i in range(0,5):
    if(pan[i].isdigit()):
        k=1
        break
    
for i in range(5,9):
    if(pan[i].isalpha()):
        k=1
        break
    
if(pan[9].isdigit()):
    k=1

if k==1:
    print("Invalid")
else:
    print("Valid")
