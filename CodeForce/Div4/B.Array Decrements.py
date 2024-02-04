tc = int(input())
for _ in range(tc):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    diffs = []
    for ai,bi in zip(a,b):
        diffs.append(ai-bi)
    max_diff = max(diffs)

    check_minus = [e for e in diffs if e < 0]
    if check_minus:
        print('NO')
        continue
    for i in range(n):
        a[i]-=max_diff
        if a[i]<0:a[i]=0



    print('YES' if a == b else 'NO')