n,m = map(int,input().split())
a = list(map(int,input().split()))
sum_a = [0]*(n+1)
result = []
for i in range(1,n+1):
    sum_a[i] = sum_a[i-1] + a[i-1]
for _ in range(m):
    a,b = map(int,input().split())
    result.append(sum_a[b] - sum_a[a-1])
for v in result:
    print(v)