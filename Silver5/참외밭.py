board = [[0]*1001 for _ in range(1001)]
y,x = 500,500

#1,2,3,4 = 동 서 남 북
dy = [0,0,1,-1]
dx = [1,-1,0,0]
p = int(input())

for i in range(6):
    direction, l = map(int,input().split())
    direction-=1
    board[y][x] = 1
    for _ in range(l-1):
        y+=dy[direction]
        x+=dx[direction]
        board[y][x] = 1
    print(y,x)


area = 0
for i in range(len(board)):
    u,v = -1,-1
    for j in range(len(board[i])):
        if board[i][j]==1:
            u = j
            break
    for j in range(len(board[i])):
        if board[i][j]==1:
            v = j
    if u!=-1 and v!=-1:
        area+=(v-u+1)
print(area)
