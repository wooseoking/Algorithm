import math

a,b,c = map(int,input().split())
ans = (c -b)/(a-b)
ans = math.ceil(ans)
print(ans)