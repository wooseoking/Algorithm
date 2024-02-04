tc = int(input())
for _ in range(tc):
    n,k = map(int,input().split())
    a = list(input())
    cnt_white = []
    l,r = 0,k-1
    cnt = a[0:k].count('W')
    cnt_white.append(cnt)

    while True:

        r+=1
        if r == n:break

        if a[r] == 'W':cnt+=1
        if a[l] == 'W':cnt-=1
        l+=1
        cnt_white.append(cnt)
        if l == n:break

    print(min(cnt_white))