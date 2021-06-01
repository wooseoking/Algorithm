import sys
sys.setrecursionlimit(400000000)
n,k = map(int,input().split())
ans = []
arr = [i for i in range(1,n+1)]

def go(K):
    if len(ans) == n:return
    X = max(arr) -1
    if K-X>=0:
        ans.append(X+1)
        arr.remove(X+1)
        go(K-X)
    else:
        ans.append(K+1)
        arr.remove(K+1)
        ans.extend(arr)
        return
go(k)
for v in ans:
    print(v,end=' ')