n,m =map(int,input().split())
weight = [0]*(n+1)
value = [0]*(n+1)
bags = []
result = []

for i in range(1,n+1):
    w,v = map(int,input().split())
    weight[i] = w
    value[i] = v

for _ in range(m):
    bags.append(int(input()))


d = [[0] * (10 ** 6 + 1) for _ in range(n + 1)]
for idx in range(1, n + 1):
    for j in range(1,10**6+1):
        d[idx][j] = d[idx - 1][j]
        if j-weight[idx]>=0:
            d[idx][j] = max(d[idx][j], d[idx - 1][j - weight[idx]] + value[idx])


for i,limit in enumerate(bags):
    result.append((d[n][limit]/limit,i+1))
result.sort(key=lambda x:(-x[0],x[1]))
print(result[0][1])