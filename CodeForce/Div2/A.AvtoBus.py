import math
import sys


def solution(a, b, n):
    i = 0
    while i * a <= n:
        if (n - (i * a)) % b == 0:
            return i,int(((n - (i * a)) / b))
        i = i + 1

    return -1,-1



t = int(input())
a,b = 6,4
for _ in range(t):
    n = int(sys.stdin.readline())
    x0,y0=solution(4,6,n)
    if x0 ==-1 and y0==-1:
        print(-1)
        continue
    print(x0,y0)
    res = [(x0,y0)]
    x = x0-b*t//n
    y = y0+a*t//n
    while True:
        t+=1
        if not x>=0 and y>=0:break
        print(x,y)
        res.append((x,y))
    print(res)

