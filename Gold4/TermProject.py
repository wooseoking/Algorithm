import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline
t = int(input())

def dfs(now):
    global ans
    visit[now]=True
    visitStack.append(now)
    next = a[now]
    if visit[next]:
        if next in visitStack:
            ans += visitStack[visitStack.index(next):]
            return
    else: dfs(next)


for _ in range(t):
    n = int(input())
    a = [0] + list(map(int,input().split()))

    ans = []
    visit = [False] * (n + 1)

    for i in range(1,n+1):
        if visit[i]:continue
        visitStack = []
        dfs(i)
    print(n-len(ans))