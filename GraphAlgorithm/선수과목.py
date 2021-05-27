import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
indegree = [0]*(n+1)
d = [1]*(n+1)
a = [[] for _ in range(n+1)]
for _ in range(m):
    v1,v2 = map(int,input().split())
    a[v1].append(v2)
    indegree[v2]+=1
q = deque()
for i in range(1,n+1):
    if indegree[i]==0:
        q.append(i)

while q:
    now = q.popleft()
    for next_ in a[now]:
        indegree[next_]-=1
        d[next_] = d[now] +1
        if indegree[next_] ==0:
            q.append(next_)
for v in d[1:]:
    print(v,end=' ')