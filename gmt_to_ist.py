days=['Sunday','Monday','Tuesday','Wednessday','Thursday','Friday','Saturday']
day=input().rstrip()
hours_min=int(input())*60
minutes=int(input())
total=hours_min+minutes+330
if 0<hours_min<24*60 and 0<m<60 and day in days:
    if total>=1440:
        for i in range(len(days)-1):
            if day==days[i]:
                print(days[i+1])
                break
        print(total//60-24)
        print(minutes-(60*(m//60)))
    else:
        print(day)
        print(total//60)
        print(minutes-(60*(m//60)))
else:
    print("Invalid input")
    
