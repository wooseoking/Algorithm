N = 100
dy = [-1,1,0,0]
dx = [0,0,-1,1]
ly = [-1,-1,-1,0,1,1,1,0]
lx = [-1,0,1,1,1,0,-1,-1]
board = [[False] * (N+1) for _ in range(N+1)]
line = [[False] * (N+1) for _ in range(N+1)]


def inside(y, x):
    return 0 <= y <=N and 0 <= x <=N


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0

    # 시작접 2배스케일링
    cX, cY, iX, iY = characterX * 2, characterY * 2, itemX * 2, itemY * 2

    #스케일 *2 배로 늘린곳에 사각형 색칠
    for x1, y1, x2, y2 in rectangle:
        X1,Y1,X2,Y2 = x1*2,y1*2,x2*2,y2*2

        for y in range(Y1,Y2+1):
            for x in range(X1,X2+1):
                board[y][x] = True

    #라인만 색칠하기
    for y in range(N+1):
        for x in range(N+1):
            if not board[y][x]:continue
            for k in range(8):
                ny,nx = y+ly[k],x+lx[k]
                if not inside(ny,nx) or not board[ny][nx]:
                    line[y][x] = True
                    break


    #BFS
    visited = [[False]*(N+1) for _ in range(N+1)]
    q = [(cY,cX,0)]
    visited[cY][cX] = True

    while q:
        y,x,cnt = q.pop(0)
        if y==iY and x==iX:
            answer = cnt//2
            break

        for k in range(4):
            ny,nx = y+dy[k],x+dx[k]
            if inside(ny,nx) and not visited[ny][nx] and line[ny][nx]:
                visited[ny][nx] = True
                q.append((ny,nx,cnt+1))

    return answer