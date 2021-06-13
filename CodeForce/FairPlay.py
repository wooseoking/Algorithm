t = int(input())
for _ in range(t):
    a = list(map(int,input().split()))
    x1 = max(a[0],a[1])
    x2 = max(a[2],a[3])
    a.sort(reverse=True)
    if x1 ==a[0] and x2 == a[1] or x1==a[1] and x2==a[0]:
        print("YES")
    else:print("NO")