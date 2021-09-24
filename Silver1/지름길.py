import sys
input = sys.stdin.readline
n,destination = map(int,input().split())
m = 10000
d = [i for i in range(m+1)]
a = []
for _ in range(n):
    x,y,cost = map(int,input().split())
    a.append((x,y,cost))
a.sort(key=lambda l : l[0])

for i in range(1,destination+1):
    d[i] = min(d[i],d[i-1]+1)
    for x, y, cost in a:
        d[y] = min(d[x] + cost, d[y])

print(d[destination])