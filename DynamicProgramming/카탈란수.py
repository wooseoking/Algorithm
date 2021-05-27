import math
n = int(input())
ans = math.comb(2*n,n) - math.comb(2*n,n+1)
ans %= pow(10,9) + 7
print(ans)