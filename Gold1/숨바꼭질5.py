from collections import deque
start,dest= map(int,input().split())
q = deque()
q.append((start,0))
ans = -1

while q:
    now,cnt = q.popleft()
    if cnt>10:break
    destination = dest
    for i in range(1,cnt+1):
        destination+=i

    if now>500000 or now <0:continue

    if now == destination:
        ans = cnt
        break
    q.append((now+1,cnt+1))
    q.append((now-1,cnt+1))
    q.append((now*2,cnt+1))
print(ans)