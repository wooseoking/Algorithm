hour , minute , sec = map(int,input().split())
c = int(input())
for _ in range(c):
    sec+=1
    if sec==60:
        minute+=1
        sec = 0
    if minute == 60:
        hour+=1
        minute = 0
    if hour == 24:
        hour = 0
print(hour,minute,sec)