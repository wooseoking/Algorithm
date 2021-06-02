import math

n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))
a.sort()
d = []
for v1,v2 in zip(a[1:],a[:]):
    d.append(v1-v2)
gcd = d[0]
for i in range(1,len(d)):
    gcd = math.gcd(gcd,d[i])
total = (a[-1] - a[0])//gcd
ans = total - len(d)
print(ans)