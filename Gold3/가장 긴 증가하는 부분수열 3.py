import bisect

n = int(input())
a = list(map(int,input().split()))
d = [0]*n
result = []
for i in range(n):
    if not result or result[-1] < a[i]:
        result.append(a[i])

    idx = bisect.bisect_left(result,a[i])
    result[idx] = a[i]
    d[i] = idx+1
print(max(d))
