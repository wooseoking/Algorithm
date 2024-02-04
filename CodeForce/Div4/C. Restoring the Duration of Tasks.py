import re

tc = int(input())
for _ in range(tc):
    n = int(input())
    s = list(map(int,input().split()))
    f = list(map(int,input().split()))
    res = []

    for i in range(n):

        if i == 0:
            res.append(f[i]-s[i])
        else:
            if s[i] <= f[i-1]:
                res.append(f[i]-f[i-1])
            else:
                res.append(f[i]-s[i])

    print(*res)