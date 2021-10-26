import copy

dy = [0] + [0,-1,-1,-1,0,1,1,1]
dx = [0] + [-1,-1,0,1,1,1,0,-1]

dig_y = [1,1,-1,-1]
dig_x = [-1,1,1,-1]

N,M = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(N)]
query =[]
for _ in range(M):
    d,s = map(int,input().split())
    query.append((d,s))

def inside(y,x):
    return 0<=y<N and 0<=x<N

def simulate(a,cloud,query,depth):
    global M
    if depth == M:
        sum_ = 0
        for i in range(N):
            for j in range(N):
                sum_+=a[i][j]

        return sum_

    visit_cloud = [[False]*N for _ in range(N)]

    d,s = query[depth]

    #구름이동
    for v in cloud:
        for _ in range(s):
            v[0]+=dy[d]
            v[0]%=N
            v[1]+=dx[d]
            v[1]%=N

    #구름 비내리기
    for y,x in cloud:
        visit_cloud[y][x] =True
        a[y][x]+=1
    #대각방향 계산
    for y,x in cloud:
        cnt = 0
        for k in range(4):
            ny,nx = y+dig_y[k],x+dig_x[k]
            if not inside(ny,nx):continue
            if a[ny][nx]>0:cnt+=1
        a[y][x]+=cnt
    #새로운 먹구름
    nextcloud = []
    for i in range(N):
        for j in range(N):
            if visit_cloud[i][j]:continue
            if a[i][j]>=2:
                nextcloud.append([i,j])
                a[i][j]-=2

    return simulate(a,nextcloud,query,depth+1)

def getsum(a):
    ret = 0
    for i in range(N):
        for j in range(N):ret+=a[i][j]
    return ret

if __name__ == '__main__':
    cloud = [[N-1,0],[N-1,1],[N-2,0],[N-2,1]]

    ans = simulate(a,cloud,query,0)
    print(ans)
