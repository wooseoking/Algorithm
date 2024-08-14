n,m = map(int,input().split())
a = [i for i in range(1,n+1)]
res = []

def pick(k):
    if k == m:
        print(' '.join(map(str,res)))
        return

    for i in range(n):
        res.append(a[i])
        pick(k+1)
        res.pop(-1)

pick(0)