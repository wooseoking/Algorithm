import sys
sys.setrecursionlimit(100000000)
input = sys.stdin.readline
n,m = map(int,input().split())
board = [list(input().strip()) for _ in range(n)]
d = [[-1]*m for _ in range(n)]

#d :-1이면 방문한번도 안함, 0이면 갈수 없음, 1이면 갈수있음
def go(y,x):
    #Success
    if y<0 or y>=n or x<0 or x>=m:return 1
    if d[y][x]!=-1:return d[y][x]
    d[y][x] = 0
    if board[y][x]=="U":
        d[y][x] = go(y-1,x)
    elif board[y][x] =="R":
        d[y][x] = go(y,x+1)
    elif board[y][x] =="D":
        d[y][x] = go(y+1,x)
    elif board[y][x] == "L":
        d[y][x] = go(y,x-1)

    return d[y][x]

for i in range(n):
    for j in range(m):
       d[i][j] = go(i,j)
ans = 0
for row in d:
    ans += row.count(1)
print(ans)
print(d)