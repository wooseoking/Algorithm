from collections import deque
n = 5
dy = [-1,1,0,0]
dx = [0,0,-1,1]

def inside(y,x):
    return 0<=y<n and 0<=x<n

def bfs(a):
    location = []

    for i in range(n):
        for j in range(n):
            if a[i][j]=='P':location.append((i,j))

    for sy,sx in location:
        q = deque()
        d = [[-1]*n for _ in range(n)]
        d[sy][sx] = 0
        q.append((sy,sx))

        while q:
            y,x = q.popleft()
            if d[y][x]!=0 and a[y][x]=='P':
                if d[y][x]<=2:return False

            for k in range(4):
                ny,nx = y+dy[k] , x+dx[k]
                if not inside(ny,nx):continue
                if d[ny][nx]!=-1:continue
                if a[ny][nx]=='X':continue
                d[ny][nx] = d[y][x]+1
                q.append((ny,nx))

    return True


def solution(places):
    answer = []
    for map in places:
        if bfs(map):answer.append(1)
        else:answer.append(0)
    return answer
