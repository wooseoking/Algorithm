tc = int(input())
for _ in range(tc):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    ans = 0
    for i in range(0,n,2):
        ans += (a[i]+a[i+1])//k

    ans2 = sum(a)//k
    print(max(ans,ans2))