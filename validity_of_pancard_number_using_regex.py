import re
pan=input()
if re.match("^[A-Z]{5}[0-9]{4}[A-Z]$",pan):
    print("Matched")
else:
    print("Not Matched")
