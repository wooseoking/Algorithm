import sys
input = sys.stdin.readline
n,m = map(int,input().split())
CLASS = list(map(int,input().split()))
CLASS.insert(0,0)
d = [[] for _ in range(m+1)]
Students = [set() for _ in range(n+1)]
#1차전
for student in range(1,n+1):
    student_want = list(map(int,input().split()))
    for ele in student_want:
        if ele==-1:continue
        d[ele].append(student)

for i in range(1,m+1):
    if len(d[i]) <= CLASS[i]:
        for who in d[i]:
            Students[who].add(i)

#2차전
for student in range(1,n+1):
    student_want = list(map(int,input().split()))
    student_want.pop(-1)
    for ele in student_want:
        d[ele].append(student)
for i in range(1,m+1):
    if len(d[i]) <= CLASS[i]:
        for who in d[i]:
            Students[who].add(i)

for i in range(1,n+1):
    if len(Students[i])==0:
        print("망했어요")
    else:
        temp_list = list(Students[i])
        temp_list.sort()
        for ele in temp_list:
            print(ele,end=' ')