dy = [-1,1,0,0]
dx = [0,0,-1,1]

def inside(y,x):
    return 0<=y<6 and 0<=x<6

def dfs(y,x,board,visited,color,erase):
    if visited[y][x]:return
    visited[y][x] = True
    erase.append((y,x))
    for k in range(4):
        ny,nx = y +dy[k],x+dx[k]
        if not inside(ny,nx):continue
        if board[ny][nx]== color and not visited[ny][nx]:
            dfs(ny,nx,board,visited,color,erase)

def simulate(board):
    Success = False
    visited = [[False]*6 for _ in range(6)]
    Delete_mac = [[False]*6 for _ in range(6)]
    #터질 마카롱 후보
    for i in range(6):
        for j in range(6):
            if board[i][j]!=0 and not visited[i][j]:
                erase = []
                dfs(i,j,board,visited,board[i][j],erase)
                if len(erase)>=3:
                    Success = True
                    for y,x in erase: Delete_mac[y][x] = True


    #터진게없으면 종료
    if not Success:return

    #터트려
    for i in range(6):
        for j in range(6):
            if Delete_mac[i][j]:board[i][j]=0

    #마카롱 내리기
    for j in range(6):
        stack = []
        for i in range(5,-1,-1):
            if board[i][j]!=0:
                stack.append(board[i][j])
        for i in range(5,-1,-1):
            board[i][j] = 0
        idx = 5
        while stack:

            board[idx][j] = stack.pop(0)
            idx-=1
    nb = board
    return simulate(nb)


def solution(macaron):

    board = [[0]*6 for _ in range(6)]

    for location,color in macaron:
        x = location - 1
        y = 0
        while True:
            y+=1
            if not inside(y,x):break
            if board[y][x]!=0:break

        y-=1
        board[y][x] = color
        simulate(board)


    return [''.join(map(str,v)) for v in board]

ans = solution([[1,1],[1,2],[1,4],[2,1],[2,2],[2,3],[3,4],[3,1],[3,2],[3,3],[3,4],[4,4],[4,3],[5,4],[6,1]])
print(ans)