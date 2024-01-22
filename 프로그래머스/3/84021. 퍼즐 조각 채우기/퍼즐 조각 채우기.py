dy = [-1,1,0,0]
dx = [0,0,-1,1]
def inside(y,x,n,m):
    return 0<=y<n and 0<=x <m

# [y.x] 위치에서 color인 값의 딱맞춰진 사각형
def getPuzzleSegment(board,visitedSegment,y,x,color):
    if board[y][x] != color or visitedSegment[y][x]: return False
    elements = []
    q = []
    q.append([y,x])

    n,m = len(board) , len(board[0])
    visited = [[False]*m for _ in range(n)]
    visited[y][x] = True
    visitedSegment[y][x] = True

    while q:
        y,x = q.pop(0)
        elements.append([y,x])

        for k in range(4):
            ny,nx = y + dy[k] ,x + dx[k]
            if not inside(ny,nx,n,m):continue
            if visited[ny][nx] or board[ny][nx] != color or visitedSegment[ny][nx]:continue
            visitedSegment[ny][nx] = True
            visited[ny][nx] = True
            q.append([ny,nx])

    return elements

def optimizeElement(element):
    minY = min(element,key=lambda x : x[0])[0]
    minX = min(element,key= lambda x :x[1])[1]

    opmizedElement = []
    for y,x in element:
        newY = y - minY
        newX = x - minX
        opmizedElement.append([newY,newX])

    return opmizedElement

def isFit(board,segment):
    boardN = max(board,key= lambda x : x[0])[0] - min(board,key= lambda x : x[0])[0] + 1
    boardM = max(board,key= lambda x : x[1])[1] - min(board,key= lambda x : x[1])[1] + 1

    b = [[1]*boardM for _ in range(boardN)]
    for y,x in board:
        b[y][x] = 0

    segN = max(segment, key=lambda x: x[0])[0] - min(segment, key=lambda x: x[0])[0] + 1
    segM = max(segment, key=lambda x: x[1])[1] - min(segment, key=lambda x: x[1])[1] + 1

    s = [[0] * segM for _ in range(segN)]
    for y, x in segment:
        s[y][x] = 1

    for _ in range(4):
        s = rotate(s)

        if len(s) == boardN and len(s[0]) == boardM:
            ok = True
            for i in range(boardN):
                for j in range(boardM):
                    if b[i][j] + s[i][j] != 1:
                        ok = False
            if ok : return True
    return False

def rotate(table):
    n,m = len(table),len(table[0])
    rotatedTable = [[0]*n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            rotatedTable[i][j] = table[j][m-i-1]
    return rotatedTable

def solution(game_board, table):
    answer = 0

    tableSegments = []
    tableN ,tableM = len(table),len(table[0])
    visitedTable = [[False]*tableM for _ in range(tableN)]

    for i in range(tableN):
        for j in range(tableM):
            if table[i][j] == 0 or visitedTable[i][j]:continue
            tableSegments.append(optimizeElement(getPuzzleSegment(table,visitedTable,i,j,1)))

    gameBoardSegments = []
    gameBoardN , gameBoardM = len(game_board),len(game_board[0])
    visitedGameBoard = [[False]*gameBoardM for _ in range(gameBoardN)]

    for i in range(gameBoardN):
        for j in range(gameBoardM):
            if game_board[i][j] == 1 or visitedGameBoard[i][j]:continue
            gameBoardSegments.append(optimizeElement(getPuzzleSegment(game_board,visitedGameBoard,i,j,0)))

    segmentsLength = len(tableSegments)
    used = [False]*segmentsLength

    #게임 보드에서 테이블 조각들 맞추어보기

    for gameBoardSegment in gameBoardSegments:
        for i in range(segmentsLength):
            if used[i] : continue
            #만약 fit 하다면 사용하기
            sement = tableSegments[i]
            if isFit(gameBoardSegment,sement):
                print(sement)
                answer += len(sement)
                used[i] = True
                break
    return answer