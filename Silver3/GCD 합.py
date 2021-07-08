import itertools
import math

t  = int(input())
for _ in range(t):
    a = list(map(int,input().split()))
    ans = 0
    for s in itertools.combinations(a[1:],2):
        ans +=math.gcd(s[0],s[1])
    print(ans)