from collections import deque
start,end= map(int,input().split())
n,m = map(int,input().split())
a = [[]for _ in range(n+1)]
d = [-1 for _ in range(n+1)]
for _ in range(m):
    x,y = map(int,input().split())
    a[x].append(y)
    a[y].append(x)

q = deque()
d[start]=0
q.append(start)
while q:
    now = q.popleft()
    for next in a[now]:
        if d[next]!=-1:continue
        d[next] = d[now] +1
        q.append(next)
print(d[end])