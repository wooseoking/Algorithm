import sys
import heapq
import math
from collections import deque
import bisect
from itertools import *
input = sys.stdin.readline
t = int(input())
n = pow(2,31)

for _ in range(t):
    a,b = map(int,input().split())
    dist = b - a
    k = None
    for i in range(1,n):
        if i*i<= dist <(i+1)*(i+1):
            k = i
            break
    ans = None
    if dist ==k*k:
        ans = 2*k-1
    elif k*k < dist <=k*k + k:
        ans = 2*k
    elif k*k +k <dist < (k+1)*(k+1):
        ans = 2*k+1

    print(ans)
