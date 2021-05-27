import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
a.sort()
if a[0]!=1:
    print(1)
else:
    Sum = a[0]
    for v in a[1:]:
        if v>Sum+1:
            break
        Sum+=v
    print(Sum+1)