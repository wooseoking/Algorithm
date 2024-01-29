# 0 nothing , 1 queen , 2 knight , 3 pawn
n , m = map(int,input().split())
queensLocations = list(map(int,input().split()))[1:]
knightsLocations = list(map(int,input().split()))[1:]
pawnsLocations = list(map(int,input().split()))[1:]

#board 초기화
board = [[0]*m for _ in range(n)]
visit = [[0]*m for _ in range(n)]

#queen 초기화
for i in range(0,len(queensLocations),2):
    y , x = queensLocations[i],queensLocations[i + 1]
    board[y-1][x-1] = 1
    visit[y-1][x-1] = 1
#knight 초기화
for i in range(0,len(knightsLocations),2):
    y , x = knightsLocations[i],knightsLocations[i + 1]
    board[y-1][x-1] = 2
    visit[y - 1][x - 1] = 1
#pawn 초기화
for i in range(0,len(pawnsLocations),2):
    y, x = pawnsLocations[i], pawnsLocations[i + 1]
    board[y - 1][x - 1] = 3
    visit[y - 1][x - 1] = 1

# queen moves
queensDirections = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
# knights moves
knightDirections = [[-1,-2],[-2,-1],[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2]]


def inside(y,x):
    return 0<=y < n and 0<=x < m

#(y,x) 에서 각 말들 움직이게 하기
def moveQueen(y,x):
    for dy,dx in queensDirections:
        k = 1
        while True:
            ny , nx = y + dy * k , x + dx * k
            if not inside(ny,nx):break
            if board[ny][nx] != 0:break
            visit[ny][nx] = 1
            k += 1

def moveKnight(y,x):
    for dy,dx in knightDirections:
        ny,nx = y + dy , x + dx
        if not inside(ny,nx):continue
        if board[ny][nx] != 0 :continue
        visit[ny][nx] = 1

# def movePawn(y,x):
#     for dy, dx in pawnsDirections:
#         ny,nx = y + dy, x + dx
#         if not inside(ny,nx):continue
#         if board[ny][nx] != 0 :continue
#         visit[ny][nx] = 1

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            moveQueen(i,j)
        elif board[i][j] == 2:
            moveKnight(i,j)
        # elif board[i][j] == 3:
        #     movePawn(i,j)

ans = sum(row.count(0) for row in visit)
print(ans)