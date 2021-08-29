import math

a = [[0]*3 for _ in range(2)]
start = list(map(int,input().split(':')))
end = list(map(int,input().split(':')))

for i in range(2):
    for j in range(3):
        if i==0: a[i][j] = start[j]
        if i==1: a[i][j] = end[j]

if a[0][0] ==a[1][0] and a[0][1] == a[1][1] and a[0][2] == a[1][2]:
    print("24:00:00")
    exit(0)

sec = 0
while True:
    if a[0][0] == a[1][0] and a[0][1] == a[1][1] and a[0][2] == a[1][2]:break
    sec+=1
    a[0][2]+=1
    if a[0][2]==60:
        a[0][2] = 0
        a[0][1]+=1
        if a[0][1]==60:
            a[0][1] = 0
            a[0][0]+=1
            if a[0][0]==24:
                a[0][0] = 0
hour,min = divmod(sec,3600)
min,sec = divmod(min,60)

hour = str(hour)
min = str(min)
sec = str(sec)

hour = hour.rjust(2,'0')
min = min.rjust(2,'0')
sec = sec.rjust(2,'0')
print(hour+':'+min+':'+sec)