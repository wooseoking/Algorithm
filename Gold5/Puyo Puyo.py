import copy

row = 12
col = 6
a = [list(input().strip()) for _ in range(row)]
c = [[False]*col for _ in range(row)]
dy = [-1,1,0,0]
dx = [0,0,-1,1]

def inside(y,x):
    return 0<=y<row and 0<=x<col

def dfs(y,x,color,temp_list):
    if c[y][x]:return
    c[y][x] =True
    temp_list.append((y,x))
    for k in range(4):
        ny = y+dy[k]
        nx = x+dx[k]
        if not inside(ny,nx):continue
        if a[ny][nx] != color:continue
        dfs(ny,nx,color,temp_list)
    if len(temp_list)>=4:
        return temp_list
    else :return None

#찾고
#없애고
#끝내고
def initc():
    for i in range(row):
        for j in range(col):
            c[i][j] = False

def makeFall():
    newa = [["."]*col for _ in range(row)]

    for j in range(col):
        stack = []
        for i in range(row):
            if a[i][j]!='.':
                stack.append(a[i][j])
        it = 0
        while stack:
            top = stack.pop()
            newa[row-1-it][j] = top
            it+=1
    return newa

ans = 0
while True:
    found = False
    break_list = []
    initc()
    for i in range(row):
        for j in range(col):
            if a[i][j]!='.':
                temp_list = []
                temp = dfs(i,j,a[i][j],temp_list)
                if temp!=None:
                    break_list.append(temp)
    if len(break_list)==0:break
    for lists in break_list:
        for y , x in lists:
            a[y][x] = '.'
    a = makeFall()
    ans+=1

print(ans)