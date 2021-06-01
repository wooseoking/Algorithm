import sys
import bisect
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))

def LIS(arr):
    l = len(arr)
    d = [0]*l
    last = []
    for i in range(l):
        if not last or last[-1] < a[i]:
            last.append(a[i])
        idx = bisect.bisect_left(last,a[i])
        d[i]= idx+1
        last[idx] = a[i]
    return d

d = LIS(a)
print(max(d))