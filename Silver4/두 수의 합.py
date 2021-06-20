from collections import deque
n,k = map(int,input().split())

d = [False]*500001
d[n] = True
q = deque()
q.append((n,0))
ans = -1
it = 0
while q:
    now,cnt = q.popleft()
    if cnt>=11:break
    if now == k + (cnt * (cnt + 1)) // 2:
        ans = cnt
        break
    if now+1<= 500000:
        q.append((now+1,cnt+1))
    if now-1>=0:
        q.append((now-1,cnt+1))
    if now*2<=500000:
        q.append((now*2,cnt+1))

print(ans)