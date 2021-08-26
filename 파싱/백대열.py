import math

a = list(map(int,input().split(':')))
GCD = math.gcd(a[0],a[1])
s1 = str(a[0]//GCD)
s2 = str(a[1]//GCD)
print(s1+':'+s2)