hour,minute = map(int,input().split())
c = int(input())

for _ in range(c):
    minute+=1
    if minute==60:
        minute = 0
        hour+=1
    if hour == 24:
        hour = 0
print(hour,minute)