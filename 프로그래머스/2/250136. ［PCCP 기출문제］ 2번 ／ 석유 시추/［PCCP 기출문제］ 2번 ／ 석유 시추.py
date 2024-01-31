dy = [-1,1,0,0]
dx = [0,0,-1,1]

def inside(y,x,n,m):
    return 0<=y<n and 0<=x<m

# y,x 위치에서 석유 좌표들 찾기
def bfs(y,x,n,m,visited,land):
    q = []
    q.append([y,x])
    visited[y][x] = True
    oil = []
    while q:
        y,x = q.pop(0)
        oil.append([y,x])
        
        for k in range(4):
            ny,nx = y + dy[k], x + dx[k]
            if not inside(ny,nx,n,m):continue
            if visited[ny][nx]:continue
            if land[ny][nx] == 0:continue
            visited[ny][nx] = True
            q.append([ny,nx])
    return oil

def solution(land):
    answer = 0
    n,m = len(land),len(land[0])
    visited = [[False]*m for _ in range(n)]
    
    # land의 2차원 배열 y,x에 오일이 있는지 확인
    oilLand = [[-1]*m for _ in range(n)]
    oilNumber = 0
    # oilNumber의 개수기
    numOfOil = dict()
    
    for i in range(n):
        for j in range(m):
            # 석유 x or 방문했으면 pass
            if land[i][j] == 0:continue
            if visited[i][j]:continue
            oil = bfs(i,j,n,m,visited,land)
            
            for oy,ox in oil:
                oilLand[oy][ox] = oilNumber
            
            numOfOil[oilNumber] = len(oil)
            oilNumber+=1
    
    res = []
    # 해당 col 에서 나오는 오일의 개수
    for x in range(m):
        oilSets = set()
        cnt = 0
        for y in range(n):
            if oilLand[y][x] == -1:continue
            oilSets.add(oilLand[y][x])
            
        for oilNum in oilSets:
            cnt += numOfOil[oilNum]
        res.append(cnt)
    
    answer = max(res)
    return answer