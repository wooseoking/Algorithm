n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]

dy = [-1,-1,1,1]
dx = [-1,1,1,-1]

l = [False]*(2*n)
r = [False]*(2*n)

def backTracking(y,x,cnt):
    if x >= n:
        y+=1
        if x % 2 == 0:
            x = 1
        else:
            x = 0

    if y>=n:
        return cnt

    ans = 0

    if board[y][x] == 1 and not l[y - x + n - 1] and not r[y + x]:
        l[y - x + n - 1] = True
        r[y + x] = True
        ans = max(ans, backTracking(y,x+2, cnt + 1))
        l[y - x + n - 1] = False
        r[y + x] = False

    return max(ans, backTracking(y,x+2, cnt))


answer = backTracking(0,0,0) + backTracking(0,1,0)

print(answer)