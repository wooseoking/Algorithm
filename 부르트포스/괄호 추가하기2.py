n = int(input())
a = list(input())

for i in range(0,n,2):
    a[i] = int(a[i])

m = (n-1)//2
ans = None

for s in range((1<<m)):
    ok = True
    for j in range(m-1):
        if(s&(1<<j) and s&(1<<j+1)):
            ok = False
    if not ok:continue

    b = a[:]

    for j in range(m):
        if (1<<j)&s:
            k = 2*j+1
            if b[k]=='+':
                b[k-1] +=b[k+1]
                b[k+1] = 0
            elif b[k]=='-':
                b[k - 1] -= b[k + 1]
                b[k] = '+'
                b[k + 1] = 0
            elif b[k]=='*':
                b[k - 1] *= b[k + 1]
                b[k] = '+'
                b[k + 1] = 0

    temp = b[0]
    for j in range(m):
        k = 2*j+1
        if b[k]=='+':
            temp+=b[k+1]
        elif b[k]=='-':
            temp -=b[k+1]
        elif b[k]=='*':
            temp *=b[k+1]

    if ans is None or ans < temp:
        ans = temp

print(ans)