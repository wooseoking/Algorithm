n = int(input())
mod = 1000000
p = 15*pow(10,5)

d = [0]*p
d[0] = 0
d[1] = 1
for i in range(2,p):
    d[i] = d[i-1] + d[i-2]
    d[i]%=mod
print(d[n%p])