from collections import deque
n = int(input())
d = [0]*(n+1)
indegree = [0]*(n+1)
time = [0]*(n+1)
a = [[] for _ in range(n+1)]

for node in range(1,n+1):
    info = list(map(int,input().split()))
    info.pop(-1)
    time[node] = info[0]
    indegree[node] = len(info)-1
    for i in info[1:]:
        a[i].append(node)

q = deque()
for i in range(1,n+1):
    if indegree[i] == 0:
        q.append(i)
        d[i] = time[i]

while q:
    now = q.popleft()
    for next in a[now]:
        indegree[next]-=1
        if d[now] + time[next] > d[next]:
            d[next] = d[now] + time[next]

        if indegree[next] == 0:
            q.append(next)
d.pop(0)
for v in d:
    print(v)