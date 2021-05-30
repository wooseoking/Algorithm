import bisect
import sys
MAX_N = 1000000
from bisect import*

def LIS(arr):
    d = [0]*n
    last = []
    for i in range(n):
        if not last or last[-1] < arr[i]:
            last.append(arr[i])
        idx = bisect_left(last,arr[i])
        last[idx] = arr[i]
        d[i] = idx +1
    return d

n = int(input())
a = list(map(int,input().split()))
d = LIS(a)
lis = max(d)
ans = []
cnt = lis
for i in range(n-1,-1,-1):
    if d[i]==cnt:
        ans.append(a[i])
        cnt-=1
ans.reverse()
print(lis)
for v in ans:
    print(v,end=' ')