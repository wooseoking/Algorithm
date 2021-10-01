import itertools
n = int(input())
a = list(map(int,input().split()))
height = [i for i in range(1,n+1)]

for s in itertools.permutations(height,n):
    tmp = list(s)
    result = []

    for i in range(1,n+1):
        idx = tmp.index(i)
        cnt = 0
        for j in range(idx):
            if tmp[j] > tmp[idx]:cnt+=1
        result.append(cnt)

    ok = True
    for v1,v2 in zip(result,a):
        if v1!=v2:ok = False
    if ok:
        for v in tmp:
            print(v,end=' ')
        exit(0)