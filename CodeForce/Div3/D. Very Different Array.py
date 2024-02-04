t = int(input())

for _ in range(t):
    n,m = map(int,input().split())

    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    a.sort()
    b.sort()

    ans = 0

    i1,i2 = 0, len(a) - 1
    j1,j2 = 0, len(b) - 1
    lenI , lenJ = abs(i1 - i2) , abs(j1 - j2)

    if lenI < lenJ:
        while i1 <= i2:

            X = abs(a[i1] - b[j2])
            Y = abs(a[i2] - b[j1])

            if X > Y:
                ans += X
                i1 += 1
                j2 -= 1
            else:
                ans += Y
                i2 -= 1
                j1 += 1
    else:
        while j1 <= j2:
            X = abs(a[j1] - b[i2])
            Y = abs(a[j2] - b[i1])

            if X > Y:
                ans += X
                j1 += 1
                i2 -= 1
            else:
                ans += Y
                j2 -= 1
                i1 += 1
    print(ans)