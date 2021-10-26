import copy
import math

dy = [-1,1,0,0]
dx = [0,0,-1,1]

N = int(input())

def inside(y,x):
    return 0<=y<N and 0<=x<N

def go(board,cnt):
    global res,N

    if cnt==5:
        max_ = -math.inf
        for i in range(N):
            for j in range(N):
                max_ = max(max_,board[i][j])

        res.append(max_)
        return

    # 0 1 2 3
    #위 아래 왼 오
    for k in range(4):
        copyboard = copy.deepcopy(board)
        visited = [[False]*N for _ in range(N)]
        if k==0:
            for j in range(N):
                for i in range(N):
                    if copyboard[i][j]==0:continue
                    y,x = i,j
                    my_num = copyboard[i][j]
                    while True:
                        y+=dy[k]
                        if not inside(y,x):break
                        if copyboard[y][x]!=0:break
                    copyboard[i][j] = 0

                    if not inside(y,x):
                        copyboard[y-dy[k]][x] = my_num
                        continue

                    if copyboard[y][x]!=0:
                        if visited[y][x]:
                            copyboard[y-dy[k]][x] = my_num
                        else:
                            if copyboard[y][x]==my_num:
                                copyboard[y][x]+=my_num
                                visited[y][x] = True
                            else:
                                copyboard[y-dy[k]][x] = my_num
        elif k==1:
            #아래로 밀기
            for j in range(N):
                for i in range(N-1,-1,-1):
                    if copyboard[i][j] == 0: continue
                    y, x = i, j
                    my_num = copyboard[i][j]
                    while True:
                        y += dy[k]
                        if not inside(y, x): break
                        if copyboard[y][x] != 0: break
                    copyboard[i][j] = 0

                    if not inside(y, x):
                        copyboard[y - dy[k]][x] = my_num
                        continue

                    if copyboard[y][x] != 0:
                        if visited[y][x]:
                            copyboard[y - dy[k]][x] = my_num
                        else:
                            if copyboard[y][x] == my_num:
                                copyboard[y][x] += my_num
                                visited[y][x] = True
                            else:
                                copyboard[y - dy[k]][x] = my_num
        elif k==2:
            #왼쪽
            for i in range(N):
                for j in range(N):
                    if copyboard[i][j] == 0: continue
                    y, x = i, j
                    my_num = copyboard[i][j]

                    while True:
                        x += dx[k]
                        if not inside(y, x): break
                        if copyboard[y][x] != 0: break


                    copyboard[i][j] = 0

                    if not inside(y, x):
                        copyboard[y][x-dx[k]] = my_num
                        continue

                    if copyboard[y][x] != 0:
                        if visited[y][x]:
                            copyboard[y][x- dx[k]] = my_num
                        else:
                            if copyboard[y][x] == my_num:
                                copyboard[y][x] += my_num
                                visited[y][x] = True
                            else:
                                copyboard[y][x - dx[k]] = my_num
        elif k==3:
            #오른쪽
            for i in range(N):
                for j in range(N-1,-1,-1):
                    if copyboard[i][j] == 0: continue
                    y, x = i, j
                    my_num = copyboard[i][j]
                    while True:
                        x += dx[k]
                        if not inside(y, x): break
                        if copyboard[y][x] != 0: break
                    copyboard[i][j] = 0

                    if not inside(y, x):
                        copyboard[y][x - dx[k]] = my_num
                        continue

                    if copyboard[y][x] != 0:
                        if visited[y][x]:
                            copyboard[y][x - dx[k]] = my_num
                        else:
                            if copyboard[y][x] == my_num:
                                copyboard[y][x] += my_num
                                visited[y][x] = True
                            else:
                                copyboard[y][x - dx[k]] = my_num
        go(copyboard,cnt+1)

    return

board_ = [list(map(int,input().split())) for _ in range(N)]
res = []
go(board_,0)
print(max(res))