import re
if(re.match(r'AV', 'AV Analytics AV')):
    print("MATCHED")
else:
    print("NOT MATCHED")
print(re.search(r'Analytics', 'AV Analytics AV Analytics'))
