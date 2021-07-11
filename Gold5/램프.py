import copy
import itertools

n,m = map(int,input().split())
a = []
for _ in range(n):
    a.append(list(map(int,input().rstrip())))
k = int(input())
if m<=k:
    if k%2==0:
        tmp = [i for i in range(m+1) if i<=m and i%2==0]
        k = max(tmp)
    else:
        tmp = [i for i in range(m + 1) if i <= m and i % 2 == 1]
        k = max(tmp)
indexes = [i for i in range(m)]
R = [i for i in range(k+1) if i%2== k%2]

L = []

for r in R:
    for candidates in itertools.combinations(indexes,r):
        lights = copy.deepcopy(a)

        for j in candidates:
            for i in range(n):
                lights[i][j] = 1 -lights[i][j]

        cnt = 0
        for i in range(n):
            if sum(lights[i])==m:cnt+=1

        L.append(cnt)

print(max(L))