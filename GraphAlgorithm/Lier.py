import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int,input().split())
a = [[] for _ in range(n+1)]
ind = [0]*(n+1)
q = deque()

for _ in range(m):
    query = list(map(int,input().split()))
    N = query[0]
    if N > 1:
        query.pop(0)
        for i in range(len(query)-1):
            v1 = query[i]
            v2 = query[i+1]
            a[v1].append(v2)
            ind[v2]+=1

for i in range(1,n+1):
    if ind[i]==0:
        q.append(i)

res= []
ok = True
for _ in range(n):
    if not q:
        ok = False
        break
    now = q.popleft()
    res.append(now)
    for next_ in a[now]:
        ind[next_]-=1
        if ind[next_] ==0:
            q.append(next_)
if ok:
    for v in res:
        print(v)
else:print(0)