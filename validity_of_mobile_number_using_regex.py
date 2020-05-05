import re
num=input()
if re.match("^[1-9][0-9]{9}$",num):
    print("Matched")
else:
    print("Not Matched")

