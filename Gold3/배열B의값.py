import copy

n,m = map(int,input().split())
a = [list(map(int,input().split()))for _ in range(n)]

def changecol(x,y):
    b = copy.deepcopy(a)
    for i in range(n):
        b[i][x] ,b[i][y] = b[i][y],b[i][x]
    return b

def changerow(x,y):
    b = copy.deepcopy(a)
    for j in range(m):
        b[x][j],b[y][j] = b[y][j],b[x][j]
    return b

def sum2D(board):
    ret = 0
    row = len(board)
    col = len(board[0])
    for i in range(row):
        for j in range(col):
            ret+=board[i][j]
    return ret

def makeB(a):
    ret = 0
    for i in range(n-1):
        for j in range(m-1):
           ret += a[i][j] + a[i+1][j] + a[i+1][j+1] + a[i][j+1]
    return ret
result = [sum2D(a)]

#행바꾸기
for i in range(n):
    for j in range(i+1,n):
        na = changerow(i,j)
        result.append(makeB(na))
#열바꾸기
for j in range(m):
    for k in range(j+1,m):
        na = changecol(j,k)
        B = makeB(na)
        result.append(makeB(na))
print(max(result))