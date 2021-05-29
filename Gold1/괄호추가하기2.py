n = int(input())
a = list(input().strip())
x = n//2
ret = []
for S in range(1<<x):
    ok = True
    for i in range(x-1):
        if S& 1<<i and S&1<<(i+1):
            ok = False
    if not ok:continue
    b = a[:]
    for i in range(x):
        if S&(1<<i):
            k = 2*i + 1
            b[k-1] = '(' + b[k-1]
            b[k+1] = b[k+1] + ')'
    num = eval(''.join(b))
    ret.append(num)
print(max(ret))