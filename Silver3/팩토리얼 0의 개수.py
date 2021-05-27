import math
import sys
input = sys.stdin.readline

n = str(math.factorial(int(input())))
arr = list(map(int,n))
ans = 0
for v in reversed(arr):
    if v==0:
        ans+=1
    else :break
print(ans)