import sys
k=0
num=input()
if len(num)!=10:
    print('Invalid')
    sys.exit(0)

if num[0]=='0':
    print('Invalid')
    sys.exit(0)

for ch
in num:
    if ch.isalpha():
        k=1

if k==0:
    print('Valid')
else:
    print('Invalid')
