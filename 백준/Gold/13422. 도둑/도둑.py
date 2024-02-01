import copy

t = int(input())

def windowSlicing(a):
    n = len(a)
    a = a + a

    cnt = 0
    window = 0
    for i in range(m):
        window += a[i]

    if window < k:
        cnt +=1

    for i in range(1,n):
        window -= a[i-1]
        window += a[i + m -1]
        if window < k:
            cnt+=1

    return cnt

for _ in range(t):
    n,m,k = map(int,input().split())
    a = list(map(int,input().split()))
    if n == m:
        if sum(a) < k:
            print(1)
            continue
    ans = windowSlicing(a)
    print(ans)