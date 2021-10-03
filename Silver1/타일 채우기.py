n = int(input())
N = 30
d = [0 for _ in range(31)]
d[2] = 3
d[0] = 1
for i in range(4,N+1):
    if i%2==0:
        d[i]+=d[i-2]*3
        j = 4
        while True:
            if i-j<0:break
            d[i]+=d[i-j]*2
            j+=2
print(d[n])