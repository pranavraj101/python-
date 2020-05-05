n = int(input())
student_marks = {}
for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
query_name = input()
nl=list(student_marks.keys())
k=0
for i in range(0,n):
        print(query_name,nl[i])
        if(query_name==nl[i]):
                k=1
ml=list(student_marks.values())
fl=ml[i]
print(fl)
print(student_marks)
avg=(fl[0]+fl[1]+fl[2])/3
avg="{0:.02f}".format(avg)
print(avg)
