from collections import deque
dy = [0,0,1,-1]
dx = [1,-1,0,0]

def inside(y,x,n,m):
    return 0<=y<n and 0<=x<m

def inputs():
    n,m = map(int,input().split())
    board_ = [list(map(int, input().split())) for _ in range(n)]
    sy, sx, sd = map(int, input().split())
    ey,ex,ed = map(int,input().split())

    return sy -1, sx-1, sd-1, ey-1, ex-1, ed-1, board_

def solve(sy,sx,sd,ey,ex,ed,board):
    n = len(board)
    m = len(board[0])
    vistied = [[[False]*4 for _ in range(m)] for _ in range(n)]
    vistied[sy][sx][sd] = True
    q = deque()
    q.append((sy,sx,sd,0))
    while q:
        y,x,d,cnt = q.popleft()

        if y==ey and x==ex and d==ed:
            return cnt
        rd ,ld = -1,-1
        #오른쪽
        if d==0:
            rd = 2
        elif d==1:
            rd = 3
        elif d==2:
            rd = 1
        elif d==3:
            rd =0
        if not vistied[y][x][rd]:
            vistied[y][x][rd] = True
            q.append((y,x,rd,cnt+1))

        #왼쪽
        if d==0:
            ld = 3
        elif d==1:
            ld = 2
        elif d==2:
            ld = 0
        elif d==3:
            ld = 1
        if not vistied[y][x][ld]:
            vistied[y][x][ld] = True
            q.append((y, x, ld, cnt + 1))

        #3칸가능
        for k in range(1,4):
            ny,nx = y,x
            ok = True
            for _ in range(k):
                ny+=dy[d]
                nx+=dx[d]
                if not inside(ny,nx,n,m):
                    ok = False
                    break
                if board[ny][nx]==1:
                    ok = False
                    break

            if ok and not vistied[ny][nx][d]:
                vistied[ny][nx][d] = True
                q.append((ny,nx,d,cnt+1))

    return 0

if __name__=='__main__':
    sy,sx,sd,ey,ex,ed,board = inputs()
    ans = solve(sy,sx,sd,ey,ex,ed,board)
    print(ans)